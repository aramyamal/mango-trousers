import math

N = 100000

aperys_constant = 0
for n in range(1, N):
    aperys_constant += 1 / n**3
    if n <= 100 and n % 10 == 0:
        print(f"n = {n}, aperys_constant = {aperys_constant}")
    elif n % 10000 == 0:
        print(f"n = {n}, aperys_constant = {aperys_constant}")
