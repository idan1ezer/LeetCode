def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res


print(singleNumber(nums = [2,2,1]))
print(singleNumber(nums = [4,1,2,1,2]))
print(singleNumber(nums = [1]))

