def twoSum(nums, target):
    cache = {}
    for i in range(len(nums)):
        if (target - nums[i] in cache):
            return cache[target - nums[i]], i
        cache[nums[i]] = i

print(twoSum(nums = [2,7,11,15], target = 9))
print(twoSum(nums = [3,2,4], target = 6))
print(twoSum(nums = [3,3], target = 6))