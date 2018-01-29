#Leetcode300,376
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        #memo[i]表示以nums[i]为结尾的最长上升子序列的长度
        memo = [ 1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i],1 + memo[j])
        res = 1
        for i in range(len(nums)):
            res = max(res,memo[i])
        return res
