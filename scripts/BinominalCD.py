# Calculate binomial cumulative distribution
import math

k = int(input("k: "))
n = int(input("n: "))
p = float(input("p: "))

def binominal_cd(k, n, p):

    if not 0 <= p <= 1:
        raise ValueError("Probability must be between 0 and 1")
    if k > n:
        raise ValueError("k cannot be greater than n")
    
    c_prob = 0
    for i in range(k + 1):

        combs = math.comb(n, i)

        prob = combs * (p ** i) * ((1 - p) ** (n - i))
        c_prob += prob
    
    return c_prob

def main(k, n, p):
    result = binominal_cd(k, n, p)
    return f"P(X <= {k}) = {result}"


print(main(k, n, p))
