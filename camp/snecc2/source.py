import random
import OpenSSL
import os
from secret import messaggio_segreto, controlla_certificato, no

assert("FLAG1" in os.environ)
flag1 = os.environ["FLAG1"]
assert("FLAG2" in os.environ)
flag2 = os.environ["FLAG2"]

def xor(a, b):
    return bytes([a[i]^b[i%len(b)] for i in range(len(a))])

def inizializza():
    try:
        res = []
        f = open('challenge_response', 'r')
        for l in f.readlines():
            res.append(int(l.strip()))
        f.close()
        return res
    except:
        res = [random.randint(1, 1000) for _ in range(100)]
        f = open('challenge_response', 'w')
        for r in res:
            f.write(str(r) + '\n')
        f.close()
        return res

def admin():
    input("Password: ")
    print("Login fallito")

def secret_comm():
    k = b"G_ab!bb_oR_oss_o"
    print(xor(messaggio_segreto, k).hex())
    res = input('> ')
    try:
        res = bytes.fromhex(res)
        cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, xor(res, k).decode())
        if not cert.has_expired():
            store = OpenSSL.crypto.X509Store()
            store.add_cert(cert)
            store_ctx = OpenSSL.crypto.X509StoreContext(store, cert)
            store_ctx.verify_certificate()
            if controlla_certificato(cert):
                print(xor(flag2.encode(), k).hex())
            else:
                print(xor(no, k).hex())
        else:
            print(xor(no, k).hex())
    except Exception as e:
        print("Qualcosa non va come previsto...")
        print(e)

def stampa_flag1():
    print(flag1)

def source():
    print(open(__file__, 'r').read())

def _exit():
    print("Bye")
    exit(0)

def menu():
    scelte = [("Login con password", admin), ("Comincia comunicazione segreta", secret_comm), ("Stampa la prima flag", stampa_flag1), ("Stampa sorgente", source), ("Esci", _exit)]
    print()
    try:
        for i in range(len(scelte)):
            print(f"{i+1}. {scelte[i][0]}")
        scelta_utente = int(input("> "))
        scelte[scelta_utente-1][1]()
    except Exception as e:
        print("Qualcosa non va come previsto...")

def main():
    responses = inizializza()
    i = random.randint(0, 99)
    print(i)
    expected = responses[i]
    try:
        given = int(input())
    except:
        given = -1
    if expected != given:
        print("No")
        exit(0)
    while True:
        menu()

if __name__ == "__main__":
    main()