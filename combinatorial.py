from math import factorial

def combinatorial(n,  k):
    n = int(input("Enter a value for n "))
    k = int(input("enter a value for k "))
    n_k = n - k
    n_factorial = 1
    for i in range(1, n + 1):
        n_factorial = n_factorial * i

    k_factorial = 1
    for i in range(1, k + 1):
        k_factorial = k_factorial * i

    nk_factorial = 1
    for i in range(1, n_k + 1):
        nk_factorial = nk_factorial * i

    result = n_factorial / (k_factorial * nk_factorial)

    return result