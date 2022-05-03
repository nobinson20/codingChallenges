# dynamic programming for dfs problem
# space complexity: O(amount), i.e., O (n)
# time complexity: O(coins * amount), i.e., O (m * n)

class Solution:
    def coinChange(self, coins: [[int]], amount: int) -> int:

        if amount == 0: return 0
        min_coin = min(coins)


        # Populated list with zeroes
        # Different approach: populate with max integers (10,000 in this case)
        #                    This way, don't need to use 'min_steps' down there
        dp = [0] * (amount + 1)

        for i in range(0, len(dp)):

            # 0) smaller than smallest coin
            if i < min_coin:
                continue

            # 1) one of coins
            elif i in coins:
                dp[i] = 1

            # 2) others
            else:
                min_steps = 10000
                for c in coins:
                    if c <= amount and dp[i - c] > 0:
                        tmp = 1 + dp[i - c]
                        if tmp < min_steps:
                            dp[i] = tmp
                            min_steps = tmp

        # for e in dp:
        #     print (e)

        return dp[amount] if dp[amount] > 0 else -1


if __name__ == '__main__':
    coins = [2]
    amount = 3

    print("answer is")
    print(Solution.coinChange(Solution, coins, amount))