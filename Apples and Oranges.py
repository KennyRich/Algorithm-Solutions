# https://www.hackerrank.com/challenges/apple-and-orange/problem


def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum(s <= a + x <= t for x in apples))
    print(sum(s <= b + x <= t for x in oranges))
