#
#
import sys


def DPChange(money, coins):
    for m in range(1, money + 1):
        bestNumCoins[m] = sys.maxint
        corrComboCoins[m] = []
        for i in range(0, len(coins)):
            if m >= coins[i]:
                if bestNumCoins[m - coins[i]] + 1 < bestNumCoins[m]: 
                    bestNumCoins[m] = bestNumCoins[m - coins[i]] + 1
                    corrComboCoins[m] \
                        = corrComboCoins[m - coins[i]] + [coins[i]]
    return (bestNumCoins[money], corrComboCoins[money])


if __name__ == '__main__':
    bestNumCoins = {0: 0}  # default value for M=0
    corrComboCoins = {0: []}  # default value for M=0
    coins = [1, 5, 10, 20, 25, 50]
    money = 100
    
    print "PROBLEM 5"
    for i in range(0, money + 1):
        print i, DPChange(i, coins)
