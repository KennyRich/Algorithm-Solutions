def oddNumbers(x, y):
    listofNum =[i for i in range(x, y+1)]
    oddNum = list(filter(lambda num: num%2 == 1, listofNum))

    return oddNum