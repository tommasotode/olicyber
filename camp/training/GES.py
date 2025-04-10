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
Che fritto misto per noi!""".split(
    "\n"
)


def to_base_18(n):
    digits = []
    while n:
        digits.append(int(n % 18))
        n //= 18
    return digits[::-1]


def from_base_18(digits):
    n = 0
    for digit in digits:
        n = n * 18 + digit
    return n.to_bytes((n.bit_length() + (n.bit_length() % 8)) // 8, "big")


def encode(s):
    final = ""
    res = ""

    # pari dispari
    for _ in range(0, len(s), 2):
        final += s[_]
    for _ in range(1, len(s), 2):
        final += s[_]

    # bytes (girati)
    i = int.from_bytes(final[::-1].encode(), "big")

    # base 18
    a = to_base_18(i)

    # righe
    for n in a:
        res += m[n] + ";"

    # toglie ultimo ;
    return res[:-1]


def decode(s):
    indici = [m.index(line) for line in s.split(";")]

    tmp = from_base_18(indici).decode()[::-1]
    res = ""
    for i in range(32):
        res += tmp[i]
        res += tmp[i + 33]

    return res


if __name__ == "__main__":
    c = "E sotto l'onda, profonda;Scampi e orate con me (saltano, danzano);Scampi e orate con me (saltano, danzano);(Le acciughe) in festa;Ecco che inizia il gran galà;Ecco che inizia il gran galà;(Le acciughe) in festa;E sotto l'onda, profonda;È il pesce tromba che sta a suonare;Scampi e orate con me (saltano, danzano);Ecco che inizia il gran galà;Insieme io e te;Che bello i pesci;(E poi) la sera;Scampi e orate con me (saltano, danzano);Ecco che inizia il gran galà;E sotto l'onda, profonda;Insieme io e te;(Perdon) la testa;(Le acciughe) in festa;Insieme io e te;È il pesce tromba che sta a suonare;(Le acciughe) in festa;Che baraonda, gioconda;Insieme io e te;Che bello i pesci;(Le acciughe) in festa;È il pesce tromba che sta a suonare;Stare a guardare;(La lu) na piena;Che baraonda, gioconda;Ecco che inizia il gran galà;Che bello i pesci;Splash!;Che baraonda, gioconda;Pepperrepeppè;È il pesce tromba che sta a suonare;Insieme io e te;Pepperrepeppè;Stare a guardare;Ecco che inizia il gran galà;Che fritto misto per noi!;(Le acciughe) in festa;Stare a guardare;È il pesce tromba che sta a suonare;Che fritto misto per noi!;Seppie e acciughe con te (ballano);Pepperrepeppè;Che baraonda, gioconda;È il pesce tromba che sta a suonare;Stare a guardare;È il pesce tromba che sta a suonare;Con seppie e scampi saltan già;E sotto l'onda, profonda;Ecco che inizia il gran galà;Scampi e orate con me (saltano, danzano);Stare a guardare;Nella padella con la pastella;Pepperrepeppè;Ecco che inizia il gran galà;Con seppie e scampi saltan già;Che fritto misto per noi!;(Le acciughe) in festa;Insieme io e te;Che fritto misto per noi!;Con seppie e scampi saltan già;Stare a guardare;Stare a guardare;Nella padella con la pastella;(La lu) na piena;Con seppie e scampi saltan già;E sotto l'onda, profonda;Che baraonda, gioconda;(Le acciughe) in festa;(E poi) la sera;E sotto l'onda, profonda;Insieme io e te;Ecco che inizia il gran galà;Scampi e orate con me (saltano, danzano);Con seppie e scampi saltan già;Scampi e orate con me (saltano, danzano);(Perdon) la testa;E sotto l'onda, profonda;Ecco che inizia il gran galà;Pepperrepeppè;Con seppie e scampi saltan già;Che bello i pesci;È il pesce tromba che sta a suonare;(Le acciughe) in festa;È il pesce tromba che sta a suonare;(La lu) na piena;Stare a guardare;Nella padella con la pastella;(La lu) na piena;Con seppie e scampi saltan già;(Le acciughe) in festa;Insieme io e te;Nella padella con la pastella;Pepperrepeppè;Con seppie e scampi saltan già;(Perdon) la testa;Con seppie e scampi saltan già;Insieme io e te;Che bello i pesci;Seppie e acciughe con te (ballano);Scampi e orate con me (saltano, danzano);Ecco che inizia il gran galà;Scampi e orate con me (saltano, danzano);Che bello i pesci;Splash!;(E poi) la sera;Ecco che inizia il gran galà;Scampi e orate con me (saltano, danzano);Con seppie e scampi saltan già;Pepperrepeppè;Splash!;Pepperrepeppè;Scampi e orate con me (saltano, danzano);Con seppie e scampi saltan già;(Perdon) la testa;(La lu) na piena;(Perdon) la testa;(E poi) la sera;Con seppie e scampi saltan già;Nella padella con la pastella"

    print(decode(c))
