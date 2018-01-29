#Leetcode416,322,377,474,139,494
class Solution:
    def canPartition(self, nums):#记忆化搜索
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum1 = sum(nums)
        if sum1%2 != 0:
            return False
        global memo
        # memo[i][c]表示使用索引为[0...i]的这些元素,是否可以完全填充一个容量为c的背包
        # -1 表示未计算,0表示不可以填充,1表示可以填充
        memo = [[-1 for i in range(sum1 // 2 + 1)] for j in range(len(nums))]
        return self.tryPartition(nums, len(nums) - 1, sum1 // 2)

    def tryPartition(self, nums, index, sums):  # 使用nums[0...index],是否可以填充一个容量为sum的背包
        if not sums:
            return True
        if sums < 0 or index < 0:
            return False
        if memo[index][sums] != -1:
            return memo[index][sums] == 1
        memo[index][sums] = 1 if self.tryPartition(nums, index - 1, sums) or self.tryPartition(nums, index - 1, sums - nums[index]) else 0
        return memo[index][sums] == 1

class Solution:
    def canPartition(self, nums):#动态规划
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum1 = sum(nums)
        if sum1%2 != 0:
            return False
        n = len(nums)
        C = sum1//2
        memo = [ False for i in range(C+1)]
        for i in range(C+1):
            memo[i] = (nums[0] == i)
        for i in range(1,n):
            for j in range(C,nums[i]-1,-1):
                memo[j] = memo[j] or memo[j-nums[i]]
        return memo[C]
