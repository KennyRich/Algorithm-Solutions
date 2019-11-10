#This is a solution to the GoldmanSachs algorithm problem

def stringFormattedWeeklyPrices(dailyPrices):
    size = dailyPrices
    result = []
    n = 0
    y = 7
    while n < size :
        output = sum(dailyPrices[n:y])
        result.append(str(round(output, 2)))

    return result