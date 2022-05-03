# Category: Dynamic Programming
# Difficulty: Easy
#
# There are four operations that can be done
# on input number 'X'
# 1. -1
# 2. Divide by 2, if the remainder is 0
# 3. Divide by 3, (same as above)
# 4. Divide by 5, (same as above)
#
# What is the minimum steps to make the number
# 'X' to 1.
#
# Example:
# For 26, it takes 3 steps to make it to one.
# 26 - 1 = 25
# 25 / 5 = 5
# 5 / 5 = 1



def MakeToOne(x:int) ->int:
  # To work on 30000th number, we need one more
  # additional space
  dp = [0] * 30001

  for cur in range(2, x+1):

    # -1 operation can apply to any number
    dp[cur] = dp[cur-1] + 1

    # when /2 operation can be applied,
    # compare the steps taken to it + 1 with
    # steps taken to previous number (+ 1: done above)
    if cur % 2 == 0:
      dp[cur] = min(dp[cur], dp[cur//2]+1)

    if cur % 3 == 0:
      dp[cur] = min(dp[cur], dp[cur//3]+1)
    
    if cur % 5 == 0:
      dp[cur] = min(dp[cur], dp[cur//5]+1)

  return dp[cur]

if __name__ == "__main__":
  x = 26
  print(MakeToOne(26))
  
