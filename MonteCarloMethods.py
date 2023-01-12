import random
import statistics as stats
import math
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

def plot_metropolis_hastings(f, N=100000, sampling_std = 0.2):
    sampled_x = []
    sampled_y = []
    
    current_state = 1
    
    for i in range(N):
        proposed_state = np.random.normal(loc=current_state, scale = sampling_std)
        r_f = f(proposed_state)/f(current_state)
        r_g = scipy.stats.norm(loc = proposed_state, scale = sampling_std).pdf(current_state) * scipy.stats.norm(loc = current_state, scale = sampling_std).pdf(proposed_state)
        if np.min([r_f*r_g, 1]) == 1:
            current_state = proposed_state
            sampled_x.append(current_state)
            #sampled_y.append(f(current_state))
        else:
            if random.random() <= r_f*r_g:
                current_state = proposed_state
                sampled_x.append(current_state)
                #sampled_y.append(f(current_state))
            else:
                sampled_x.append(current_state)
                #sampled_y.append(f(current_state))
    x = np.linspace(0, 10)
    plt.plot(x, [f(i) for i in x], label = "not normalized true")
    plt.hist(sampled_x[N//100:], label = "normalized with mcmc", bins=100, density=True, histtype="step")
    plt.legend()
    plt.show()
    return

def wigner_semicircle(x, R=0.5):
    #return (2 / (math.pi * R**2)) * math.sqrt(R**2 - x**2)
    if x**2 < R**2:
        return (2 / (math.pi * R**2)) * math.sqrt(R**2 - x**2)
    else: return 0

def gaussian(x):
    return math.exp(-x**2/2)

def exponential(x, gamma = 0.2):
    if x >= 0:
        return math.exp(-gamma*x)
    else: return 0

def log_normal(x):
    if x > 0:
        return 1/(x**(1 + math.log(x)))
    else: return 0

plot_metropolis_hastings(log_normal, N= 10000)

#_____________________________________________________
def find_pi(N = 1000000):
    circle = 0
    for i in range(N):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
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

#find_pi()
#find_expval_game()