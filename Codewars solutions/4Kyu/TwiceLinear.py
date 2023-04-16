
def dbl_linear(n):
    u = []
    for i in range(n*2 //3):
        if i == 0:
            u = [1]
        else:
            u.append(2*u[i-1]+1)
            u.append(3*u[i-1]+1)
            u = list(dict.fromkeys(u))
            u.sort()
    return print(u[n])

dbl_linear(10)

# def dbl_linear(n):