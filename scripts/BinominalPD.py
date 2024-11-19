# Calculate binomial probability distribution
import math


def bpd(k, n, p):

    if not 0 <= p <= 1:
        raise ValueError("Probability must be between 0 and 1")
    if k > n:
        raise ValueError("k cannot be greater than n")
    p_prob = math.comb(n, k) * p**k * (1 - p) ** (n - k)
    return p_prob

k = int(input("k: "))
n = int(input("n: "))
p = float(input("p: "))

def main(k, n, p):
    result = bpd(k, n, p)
    return f"P(X = {k}) = {result}"

print(main(k, n, p))