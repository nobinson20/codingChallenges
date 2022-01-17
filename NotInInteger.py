# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(nums):
    # write your code in Python 3.6
    nums = list(set(nums))
    nums.sort()
    cnt = 1

    for e in nums:
        if e < 0:
            continue
        if e != cnt:
            return cnt
        if e > 0:
            cnt += 1


    return cnt