"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
Leetcode1
"""
#类似Leetcode15，18，16
def twoSum(nums,target):
    #时间复杂度0(n)
    #空间复杂度0(n)
    record = {}
    for i in range(len(nums)):
        complement = target - nums[i]#看complement在dict中是否存在
        if complement in record:
            res = [record[complement],i]
            return res
        record[nums[i]] = i
    return "the input has no solution"
