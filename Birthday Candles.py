def birthdayCakeCandles(ar):
    count=0
    big = max(ar)
    for i in range(len(ar)):
        if(ar[i]==big):
            count+=1
    return count