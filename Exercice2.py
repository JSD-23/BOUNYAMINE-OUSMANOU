def maxProfit(prix):
    size = len(prix)
    if size <= 1:
        return 0
    profit = 0
    acheter = prix[0]

    for i in range(1, size):
        vendre = prix[i]
        if vendre > acheter:
            gain = vendre - acheter
            profit = max(profit, gain)
        else:
            acheter = vendre
    return profit
