# Calculate binomial cumulative distribution
import math

k = int(input("k: "))
p = float(input("p: "))
Px = float(input("P(X): "))

def binominal_cd(k, p, Px):
    c_prob = 0
    for n in range(k+1, 10000):
        for i in range(k + 1):

            combs = math.comb(n, i)

            prob = combs * (p ** i) * ((1 - p) ** (n - i))
            c_prob += prob
            
        if c_prob >= Px:
            return f"when n = {n}, P(X <= {k}) >= {Px}"
    return c_prob

def main(k, p, Px):
    result = binominal_cd(k, p, Px)
    return result


print(main(k, p, Px))
