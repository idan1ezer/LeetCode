def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


print(searchInsert(nums = [1,3,5,6], target = 5))
print(searchInsert(nums = [1, 3, 5, 6], target = 2))
print(searchInsert(nums = [1,3,5,6], target = 7))
print(searchInsert(nums = [1,3,5,6], target = 0))
print(searchInsert(nums = [1], target = 0))