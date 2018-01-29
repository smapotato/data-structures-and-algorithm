#Leetcode435
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):#动态规划
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key = lambda x : (x.start,x.end))
        #memo[i]表示使用intervals[0...i]的区间能构成的最长不重叠区间序列
        memo = [ 1 for i in range(len(intervals))]
        for i in range(1,len(intervals)):
            for j in range(i):
                if intervals[i].start >= intervals[j].end:
                    memo[i] = max(memo[i],1 + memo[j])
        res = 0
        for i in range(len(intervals)):
            res = max(res,memo[i])
        return len(intervals)-res

class Solution:#贪心算法
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key = lambda x: (x.end,x.start))
        res = 1
        pre = 0
        for i in range(1,len(intervals)):
            if intervals[i].start >= intervals[pre].end:
                res += 1
                pre = i
        return len(intervals) - res
