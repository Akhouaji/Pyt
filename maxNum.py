def maxNum(nums):
    nums.sort()
    return nums[-1]
nums1=[3, 5, 2, 9 ,7]
print(maxNum(nums1))

def maxNum2(numss):
    return max(numss)

nums2 = [4, 8, 7, 1, 15]
print(maxNum2(nums2))