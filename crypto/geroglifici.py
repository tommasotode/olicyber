import string

alphabet = string.ascii_letters + string.digits + '_{}!'
emojialphabet = "🐷🐐🐣🐞🦐🦕🐼🐍🐉🐥🐎🦆🐡🐃🦇🦟🦘🦢🐏🐦🐔🐁🐀🐯🐢🐫🐑🐽🐺🦄🐶🐙🦒🐻🐗🐆🐮🦑🦜🐬🦍🐖🦞🐴🦏🐋🦁🐌🐰🦙🦔🐊🐳🦓🐇🦋🦈🦝🐧🦅🐟🐛🐂🐭🐅🐝"

a = {}
for i,j in zip(alphabet, emojialphabet):
    a[j] = i

encflag = "🦕🦆🐷🐼🐭🐷🐃🐣🐍🦐🐂🐼🦆🐉🐂🦐🐼🐉🐫🐉🐂🐣🦇🐃🦇🐏🐣🦐🐁🐷🐃🦇🐂🐺🦐🐏🐷🦢🦐🐅"
for i in encflag:
    print(a[i], end="")