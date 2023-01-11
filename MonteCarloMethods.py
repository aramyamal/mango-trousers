import random
import statistics as stats

def find_pi(N = 10000):
    circle = 0
    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y **2 <= 1:
            circle = circle + 1
    return print(f"The calculated value of Pi with N = {N} is {4 * circle / N}")


#If I play a game with P(win) = p, and each round the game ends when I lose 2 times in a row,
#whats the expected value of the number of rounds ?
def find_expval_game(p = 0.5, N = 100000):
    rounds = []
    for i in range(N):
        r = 0
        n_loss = 0
        while n_loss != 2:
            r += 1
            if random.random() < p:
                n_loss = 0
            else:
                n_loss += 1
        rounds.append(r)
    return print(f"The expected value of rounds for P(win) = {p} is {stats.mean(rounds)}")

find_pi()
find_expval_game()