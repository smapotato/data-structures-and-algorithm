"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
"""
#Leetcode49
def fourSumCount(A, B, C, D):
    #时间复杂度0(n)
    record = {}
    for i in D:#把C,D中的元素组合放在dict中
        for j in C:
            if i+j in record:
                record[i+j] += 1
            else:
                record[i+j] = 1
    res = 0
    for i in C:
        for j in D:
            if -i-j in record:
                res += record[-c-d]
    return res
