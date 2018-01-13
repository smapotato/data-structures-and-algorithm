#leetcode46,47
class Solution(object):
    used = [False for _ in range(len(nums))]
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums,[],res)
        return res
    def dfs(self,nums,path,res):
        if not nums:
            res.append(path)
            return res
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
