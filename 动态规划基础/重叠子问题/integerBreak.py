#Leetcode343,279,91,62,63
class Solution:#自顶向下的记忆化搜索
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        global memo
        memo = [ -1 for i in range(n+1)]
        return self.breakInteger(n)
    def breakInteger(self,n):#将n进行分割，可以获得的最大乘积
        if n == 1:
            return 1
        if memo[n] != -1:
            return memo[n]
        res = -1
        for i in range(1,n):
            res = max(res,i*(n-i),i*self.breakInteger(n-i))
        memo[n] = res
        return res



class Solution1:#自底向上的动态规划
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [ -1 for i in range(n+1)]#memo[i]表示将i分割后得到的最大乘积
        memo[1] = 1
        for i in range(2,n+1):#求解memo[i]
            for j in range(1,i):#j+(i-j)
                memo[i] = max(memo[i],j*(i-j),j*memo[i-j])
        return memo[n]
