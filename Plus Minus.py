def plusMinus(arr):
    zero = 0
    positive = 0
    negative = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            positive += 1
        elif arr[i] == 0:
            zero += 1
        elif arr[i] < 0:
            negative += 1
    p = positive / len(arr)
    n = negative / len(arr)
    z = zero / len(arr)

    print(p)
    print(n)
    print(z)