def distributeCoins(price):
    coins = [2, 1, 0.5, 0.2, 0.1, 0.05]
    coinDistro = {
        2: 0,
        1: 0,
        0.5: 0,
        0.2: 0,
        0.1: 0,
        0.05: 0
    }

    i = 0

    while(price > 0):
        if(price >= coins[i]):
            # select the coin
            print(coins[i])
            price = round(price, 2) - round(coins[i], 2)
            price = round(price, 2)
            coinDistro[coins[i]] += 1
        else:
            i += 1
    return coinDistro


price = input("Price: ")
print(distributeCoins(float(price)))
