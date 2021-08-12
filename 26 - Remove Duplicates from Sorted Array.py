def removeDuplicates(nums):
    if (not nums):
        return 0

    curIndex = 0
    for i in range(1, len(nums)):
        if (nums[i] != nums[curIndex]):
            curIndex += 1
            nums[curIndex] = nums[i]

    return curIndex + 1,nums


print(removeDuplicates(nums = [1,1,2]))
print(removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))