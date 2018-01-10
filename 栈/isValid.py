#Leetcode20,150,71
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {"(":")","{":"}","[":"]"}
        for i in s:
            if i in d.keys():
                stack.append(i)
            else:
                if stack:
                    a = stack.pop()
                    if i != d[a]:
                        return False
                else:
                    return False
        return stack == []
