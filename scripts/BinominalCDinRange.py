# Calculate binomial cumulative distribution
import math

a = int(input("min: "))
b = int(input("max: "))
n = int(input("n: "))
p = float(input("p: "))

def binominal_cd(a, b, n, p):

    if not 0 <= p <= 1:
        raise ValueError("Probability must be between 0 and 1")
    if a > n:
        raise ValueError("min cannot be greater than n")
    if b > n:
        raise ValueError("max cannot be greater than n")
    
    c_prob = 0
    for i in range(a+1, b+1):

        combs = math.comb(n, i)

        prob = combs * (p ** i) * ((1 - p) ** (n - i))
        c_prob += prob
    
    return c_prob

def main(a, b, n, p):
    result = binominal_cd(a, b, n, p)
    return f"P({a} <= X <= {b}) = {result}"


print(main(a, b, n, p))
