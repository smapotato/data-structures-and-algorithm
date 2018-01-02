"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
"""
def MoveZeros(arr):
    # 时间复杂度0（n),空间复杂度0（n）
    a = []
    for i in arr:
        if i:
            a.append(i)
    return a + [0] * (len(arr) - len(a))


def move(alist):
    # 时间复杂度0（n),空间复杂度0（1）
    index = 0  # 创建一个新的索引
    for i in range(len(alist)):
        if alist[i]:
            alist[index] = alist[i]
            index += 1
    for a in range(index, len(alist)):
        alist[a] = 0
    return alist


def move1(alist):
    # 时间复杂度0（n),空间复杂度0（1）
    index = 0  # 创建一个新的索引
    for i in range(len(alist)):
        if alist[i]:
            if i != index:  # 如果全为非0元素，则不用交换
                alist[index], alist[i] = alist[i], alist[index]
                index += 1
            else:
                index += 1
    return alist

