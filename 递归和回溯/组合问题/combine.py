#Leetcode77,39,216,78,90,401
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if n <= 0 or k <= 0 or k > n:
            return res
        c = []
        self.generateCombinations(n,k,1,c,res)
        return res
    def generateCombinations(self,n,k,start,c,res):
        #当前已经找到的组合存储在c中，需要从start开始搜索新的元素
        if len(c) == k:
            res.append(list(c))#如果直接append(c),则操作c.pop()时,res同样也随之改变
            return res
        #优化：还有k-len(c)个空位，所以[i,n]中至少要有k-len(c)个元素
        #i最多为n-(k-len(c))+1
        #for i in range(n+1)[start:]
        for i in range(start,n-(k-len(c))+2):
            c.append(i)
            self.generateCombinations(n,k,i+1,c,res)#从i+1开始取
            c.pop()
