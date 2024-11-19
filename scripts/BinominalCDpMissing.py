# Calculate binomial cumulative distribution
import math

k = int(input("k: "))
n = float(input("n: "))
Px = float(input("P(X): "))

def binominal_cd(k, n, Px):
    c_prob = 0
    p = 0.0
    while p <= 1.0:
        for i in range(k + 1):

            combs = math.comb(n, i)

            prob = combs * (p ** i) * ((1 - p) ** (n - i))
            c_prob += prob
        if c_prob >= Px:
            return f"when n = {p}, P(X <= {k}) >= {Px}"
        else:
            p+=0.01
        
    return c_prob

def main(k, n, Px):
    result = binominal_cd(k, n, Px)
    return result


print(main(k, n, Px))
