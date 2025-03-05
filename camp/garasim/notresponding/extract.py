#!/usr/bin/env python3

import pyshark
import json

PCAP_FILE = 'notresponding.pcapng'

f = open("output.txt", "w")

cap = pyshark.FileCapture(
    PCAP_FILE, 
    display_filter='http.request.method == PUT',
    decode_as={'tcp.port==80': 'http'}
)

for packet in cap:
    try:
        raw_json = packet.http.file_data

        data = json.loads(raw_json)

        pos = data['pos']
        val = data['val']
        f.write(f'pos={pos}, val={val}\n')
    except (AttributeError, KeyError, json.JSONDecodeError):
        pass

f.close()