'''
    两数之和
    
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

    示例：

    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
    链接: https://leetcode-cn.com/problems/two-sum

	Given an array of integers, return indices of the two numbers such that they add up to a specific target.

	You may assume that each input would have exactly one solution, and you may not use the same element twice.

	Example:

	Given nums = [2, 7, 11, 15], target = 9,

	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
'''

def twoSum(nums, target):
    # Create an empty dictionary to store numbers and their indices
    mapping = {}

    for index, num in enumerate(nums):
        diff = target - num
        if diff in mapping:
            return [mapping[diff], index]
        mapping[num] = index

# Test the function
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Expected output: [0, 1]