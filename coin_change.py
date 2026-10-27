import matplotlib.pyplot as plt
import time

def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    opt = []
    for coin in coins:
        if coin <= amount:
            opt.append(1 + coin_change_recursive(coins, amount - coin))
    return min(opt)

def coin_change_memoized(coins, amount, memo):
    if amount == 0:
            return 0
    if amount in memo:
        return memo[amount]
    opt = []
    for coin in coins:
        if coin <= amount:
            opt.append(1 + coin_change_memoized(coins, amount - coin, memo))
    memo[amount] = min(opt)
    return memo[amount]

def coin_change_dp(coins, amount):
    dp = [0] * (amount + 1)
    dp.append(0)
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[amount]

def benchmark():
    
    target = [10, 20, 30, 40, 50] # Creates input sizes that will be used to test speed at different sizes
    naiveList = []
    memoList = [] 
    dpList = []
    
    coins = [1, 5, 10, 25]
    for n in target:
        naiveTimes = []
        memoTimes = []
        dpTimes = []


        for j in range (0, 10): # Tests each algorithm 10 times per size
            start_time = time.perf_counter()
            coin_change_recursive(coins, n)
            end_time = time.perf_counter()
            naiveTimes.append(end_time - start_time)
            start_time2 = time.perf_counter()
            memo = {}
            memo = coin_change_memoized(coins, n, memo)
            end_time2 = time.perf_counter()
            memoTimes.append(end_time2 - start_time2)
            start_time3 = time.perf_counter()
            coin_change_dp(coins, n)
            end_time3 = time.perf_counter()
            dpTimes.append(end_time3 - start_time3)
        naive_average = sum(naiveTimes) / 10
        memo_average = sum(memoTimes) / 10
        dp_average = sum(dpTimes) / 10
        naiveList.append(naive_average)
        memoList.append(memo_average)
        dpList.append(dp_average)

    # Plot Code
    plt.plot(target, naiveList, label="naive alg", color="red", marker="o")
    plt.plot(target, memoList, label="memo alg", color="green", marker="o")
    plt.plot(target, dpList, label="bottom-up alg", color="blue", marker="o")
    plt.title("Comparing Coin Change Algorithms")
    plt.xlabel("target (cents)")
    plt.ylabel("average time (seconds)")
    plt.yscale('log')
    plt.legend()
    plt.grid((True))
    plt.savefig('results.png', dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    benchmark()