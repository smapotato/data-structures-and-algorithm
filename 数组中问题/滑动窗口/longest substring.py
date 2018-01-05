"""
Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
Leetcode 3
"""
#类似Leetcode483,76
def lengthOfLongestSubstring(s):
    freq = [0]*256 #用于记录每个字符串当前出现频率，索引为每个字符串对应的ASCII码用于记录每个字符串当前出现频率，索引为每个字符串对应的ASCII码
    l,r = 0,-1 #滑动窗口为s[l..r]
    res = 0
    while l < len(s):
        # 当右边界下一个位置s[r+1]的频率为0时才右移，否则有重复字符，就右移左边界直到没有重复字符
        if r+1 < len(s) and freq[ord(s[r+1])]==0:
            r += 1
            freq[ord(s[r])] += 1
        else:
            freq[ord(s[l])] -= 1
            l += 1
        res = max(res,r-l+1)
        #  每次循环中滑动窗口内永远不会有重复字符，所以每次都可以做比较，最终res为最大值
    return res
