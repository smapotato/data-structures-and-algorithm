"""
Leetcode209
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""
def minSubArrayLen(s,nums):#时间复杂度0(n)
    l,r = 0,-1 #nums[l,r]为我们的滑动窗口
    sum = 0
    res = len(nums) + 1#不可能取到的值
    while l < len(nums):
        if r+1 < len(nums) and sum < s:
            r += 1
            sum += nums[r]
        else:
            sum -= nums[l]
            l += 1
        if sum >= s:
            res = min(res,r-l+1)
    if res == len(nums) + 1:
        return 0
    return res
print(minSubArrayLen(7,[2,3,1,2,4,3]))
