"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def twoSum(nums, target):
    for i in nums:
        for z in nums[nums.index(i) + 1:]:
            if (i + z) == target:
                if i == z:
                    pos = nums.index(i)
                    nums.remove(i)
                    return [pos, nums.index(z) + 1]
                return [nums.index(i), nums.index(z)]

