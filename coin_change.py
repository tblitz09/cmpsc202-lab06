def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    opt = []
    for i in range(1, len(coins)):
        if coins[i] <= amount:
            opt.append(1 + coin_change_recursive(amount - coins[i]))
    return opt

def coin_change_memoized(coins, amount, memo):
    if amount == 0:
        return 0
    if amount in memo:
        return memo[amount]
    opt = []
    for i in range(1, len(coins)):
        if coins[i] <= amount:
            opt.append(1 + coin_change_recursive(amount - coins[i]))
    memo[amount] = len(opt)
    return len(opt), memo

def coin_change_dp(coins, amount):
    dp = []
    dp[0] = 0
    for i in range(1, amount):
        opt = []
        for j in range(1, len(coins)):
            opt.append(1 + dp[max(i - coins[j], 0)])
    return dp
