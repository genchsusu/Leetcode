'''
寻找两个有序数组的中位数
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

简而言之中位数把一个数集划分为长度相等两部分,而这个数要比上部分数值都要大,比下部分数值都要小

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5


https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
二分法
'''

def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the shorter list.
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionx = (low + high) // 2  # Find partition in the shorter list.
        partitiony = (x + y + 1) // 2 - partitionx  # Corresponding partition in the longer list.

        # Handling edge cases for maxLeftX and minRightX.
        maxLeftX = float('-inf') if partitionx == 0 else nums1[partitionx - 1]
        minRightX = float('inf') if partitionx == x else nums1[partitionx]

        # Handling edge cases for maxLeftY and minRightY.
        maxLeftY = float('-inf') if partitiony == 0 else nums2[partitiony - 1]
        minRightY = float('inf') if partitiony == y else nums2[partitiony]

        # Checking if we've found the correct partitions.
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:  # If total length is even, return average of the two middle numbers.
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            else:  # If total length is odd, return the max of the left partitions.
                return max(maxLeftY, maxLeftX)
        # Adjusting the binary search range.
        elif maxLeftX > minRightY:
            high = partitionx - 1
        else:
            low = partitionx + 1
            

print(findMedianSortedArrays([1,2], [3, 4]))