# https://www.hackerrank.com/challenges/between-two-sets/problem


def getTotalX(a, b):
    # Write your code here
    total = sum(all(i % x == 0 for x in a) and all(x % i == 0 for x in b) for i in range(1, 101))
    return total
