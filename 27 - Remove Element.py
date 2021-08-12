def removeElement(nums, val):
    curIndex = 0

    for i in range(len(nums)):
        if(nums[i] != val):
            nums[curIndex] = nums[i]
            curIndex += 1
    return curIndex


print(removeElement(nums = [3,2,2,3], val = 3))
print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
print(removeElement(nums = [2], val = 3))