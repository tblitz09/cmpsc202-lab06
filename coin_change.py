import matplotlib as plt
import time

def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    opt = []
    for coin in coins:
        if coin <= amount:
            opt.append(1 + coin_change_recursive(coins, amount - coins))
    return len(opt)

def coin_change_memoized(coins, amount, memo):
    if amount == 0:
            return 0
    if amount in memo:
        return memo[amount]
    opt = []
    for coin in coins:
        if coin <= amount:
            opt.append(1 + coin_change_memoized(coins, amount - coin, memo))
    memo[amount] = len(opt)
    return memo[amount]

def coin_change_dp(coins, amount):
    dp = []
    dp[0] = 0
    for i in range(1, amount):
        opt = []
        for j in range(1, len(coins)):
            opt.append(1 + dp[max(i - coins[j], 0)])
    return dp

def benchmark():
    
    target = [10, 20, 30, 40, 50, 60] # Creates input sizes that will be used to test speed at different sizes
    naiveList = []
    memoList = [] 
    dpList = []
    memo = []
    coins = [1, 5, 10, 25]
    for n in target:
        naiveTimes = []
        memoTimes = []
        dpTimes = []


        for j in range (0, 10): # Tests each algorithm 10 times per size
            start_time = time.perf_counter()
            coin_change_recursive(coins, target)
            end_time = time.perf_counter()
            naiveTimes.append(end_time - start_time)
            start_time2 = time.perf_counter()
            memo = coin_change_memoized(coins, target, memo)[1]
            end_time2 = time.perf_counter()
            memoTimes.append(end_time2 - start_time2)
            start_time3 = time.perf_counter()
            coin_change_dp(coins, target)
            end_time3 = time.perf_counter()
            dpTimes.append(end_time3 - start_time3)
        naive_average = sum(naiveTimes) / 10
        memo_average = sum(memoTimes) / 10
        dp_average = sum(dpTimes)
        naiveList.append(naive_average)
        memoList.append(memo_average)
        dpList.append(dp_average)

    # Plot Code
    plt.plot(target, naiveList, label="fast average time", color="red", marker="o")
    plt.plot(target, memoList, label="fast average time", color="red", marker="e")
    plt.plot(target, dpList, label="slow average time", color="blue", marker="s")
    plt.title("Comparing fast vs slow algorithms with different size lists")
    plt.xlabel("size of list (n)")
    plt.ylabel("average time (seconds)")
    plt.legend()
    plt.grid((True))
    plt.savefig('results.png', dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    benchmark()