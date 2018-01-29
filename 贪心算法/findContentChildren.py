#Leetcode455,392
class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse=True)
        s.sort(reverse=True)
        si,gi = 0,0
        res = 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                res += 1
                si += 1
                gi += 1
            else:
                gi += 1
        return res
