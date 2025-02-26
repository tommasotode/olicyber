import numpy as np

enc = "630:624:622:612:609:624:623:610:624:624:567:631:638:639:658:593:546:605:607:585:648:636:635:704:702:687:687:682:629:699:633:639:634:637:578:622:620:617:606:615:568:633:589:587:645:639:653:654:633:634"

hash_vals = [int(x) for x in enc.split(":")]
length = len(hash_vals)

M = np.zeros((length, length), dtype=float)
for i in range(length):
    for k in range(7):
        M[i][(i + k) % length] = 1.0

S = np.array(hash_vals, dtype=float)

P = [int(round(x)) for x in np.linalg.solve(M, S)]

password = ''.join(chr(x) for x in P)
print(password)