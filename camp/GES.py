import sys

m = """Splash!
E sotto l'onda, profonda
Insieme io e te
Che bello i pesci
Stare a guardare
Che baraonda, gioconda
Pepperrepeppè
È il pesce tromba che sta a suonare
Seppie e acciughe con te (ballano)
Scampi e orate con me (saltano, danzano)
(E poi) la sera
(La lu) na piena
Ecco che inizia il gran galà
(Le acciughe) in festa
(Perdon) la testa
Con seppie e scampi saltan già
Nella padella con la pastella
Che fritto misto per noi!""".split('\n')

def to_base_18(n):
    digits = []
    while n:
        digits.append(int(n % 18))
        n //= 18
    return digits[::-1]

def encode(s):
    final = ''
    res = ''
    for _ in range(0, len(s), 2):
        final += s[_]
    for _ in range(1, len(s), 2):
        final += s[_]
    i = int.from_bytes(final[::-1].encode(), 'big')
    a = to_base_18(i)
    for n in a:
        res += m[n] + ';'
    print(res[:-1])

def decode(s):
    # Questa funzione è lasciata allo studente come esercizio
    print('unimplemented')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        #Print help
        exit(1)
    elif sys.argv[1] == 'e':
        encode(sys.argv[2])
        exit(0)
    elif sys.argv[1] == 'd':
        decode(sys.argv[2])
        exit(0)
    else:
        #Print help
        exit(2)