from sympy.ntheory.modular import solve_congruence

congruences = [
    (13, 99),
    (44, 46),
    (0, 7),
    (62, 65),
    (37, 61)
]

solution, modulus = solve_congruence(*congruences)

print(solution % 126396270)