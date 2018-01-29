#Leetcode198,213,337,309
class Solution:
    def rob(self, nums):#自顶向下的记忆化搜索
        """
        :type nums: List[int]
        :rtype: int
        """
        global memo
        memo = [-1 for i in range(len(nums))]#memo[i]表示考虑抢劫nums[i,n]所能获取的最大收益
        return self.tryRob(nums,0)
    def tryRob(self,nums,index):#考虑抢劫nums[index:]范围内的所有房子
        if index >= len(nums):
            return 0
        if memo[index] != -1:
            return 0
        res = 0
        for i in range(index,len(nums)):
            res = max(res,nums[i] + self.tryRob(nums,i+2))
        memo[index] = res
        return res
class Solution:
    def rob(self, nums):#自顶向下的记忆化搜索
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        memo = [-1 for i in range(n)]  # memo[i]表示考虑抢劫nums[i,n]内的最大收益
        memo[n-1] = nums[-1]
        for i in range(n - 1, -1, -1):  # memo[i]
            for j in range(i-1, n):
                memo[i] = max(memo[i], nums[j] + (memo[j + 2] if j + 2 < n else 0))
        return memo[0]
