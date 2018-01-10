#Leetcode347，23
import collections
import heapq
def topKFrequent( nums, k):
    c = collections.Counter(nums)
    return heapq.nlargest(k, c, c.get)
print(topKFrequent([1,1,1,2,2,3],2))
