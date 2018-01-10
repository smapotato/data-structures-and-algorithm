#Leetcode279，127，126
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        lst = []
        i = 1
        while i*i < n:
            lst.append(i*i)
            i += 1
        cnt = 0#层数，即最短路径
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()#省略重复元素
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return  cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp
s = Solution()
print(s.numSquares(13))
