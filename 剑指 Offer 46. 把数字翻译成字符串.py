def translateNum(num: int) -> int:
    nums = str(num)
    if len(nums) < 2: return 1

    dp = [0] * len(nums)
    dp[0] = 1
    if 9< int(nums[0:2]) < 26:
        dp[1] = 2
    else:
        dp[1] = 1
    for i in range(2, len(nums)):
        if 9< int(nums[i - 1:i+1]) < 26:
            dp[i] = dp[i - 2] + dp[i - 1]
        else:
            dp[i] = dp[i - 1]
    return dp[-1]
print(translateNum(506))