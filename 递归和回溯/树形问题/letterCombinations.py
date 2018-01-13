#Leetcode17,93,131
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return ""
        res = []
        self.findCombination(digits,0,"",res)
        return res
    def findCombination(self,digits,index,ls,res):
        #ls中保存了从digits[0,index-1]翻译得到的一个字母字符串
        #寻找和digits[index]匹配的字母，获得digits[0,index]翻译得到的解
        letterMap = [" ","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if index == len(digits):
            res.append(ls)
        c = digits[index]
        letters = letterMap[int(c)]
        for i in letters:
            self.findCombination(digits,index+1,ls+i,res)
#Pythonic
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])
