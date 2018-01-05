"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""
def containsNearbyDuplicate(nums,k):
    #时间复杂度0(n)
    record = {}
    for i,v in enumerate(nums):
        if v in record and i - record[v] <= k:
            return True
        record[v] = i
    return False
