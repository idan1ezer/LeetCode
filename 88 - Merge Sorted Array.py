def merge(nums1, m, nums2, n):
    while (m >= 1 and n >= 1):
        if (nums1[m - 1] >= nums2[n - 1]):
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if (n > 0):
        nums1[:n] = nums2[:n]

    return nums1


print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(merge(nums1 = [1], m = 1, nums2 = [], n = 0))
print(merge(nums1 = [0], m = 0, nums2 = [1], n = 1))