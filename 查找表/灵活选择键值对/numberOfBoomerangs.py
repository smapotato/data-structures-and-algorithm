"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
"""
#Leetcode447，149
def numberOfBoomerangs(points):
    #时间复杂度0(n^2)
    #空间复杂度0(n)
    res = 0
    for i in points:
        record = {}
        for j in points:
            dis = (i[0] - j[0]) ** 2 + (j[0] - j[1]) ** 2
            """
            if dis in record:
                if j != i:
                    record[dis] += 1
            else:
                record[dis] = 1
            """
            record[dis] = record.get(dis,0) + 1
        for i in record.values():
            """
            if i >=2:
                res += i*(i-1)
           """
            res += i(i-1)#i=1是为0
    return res
