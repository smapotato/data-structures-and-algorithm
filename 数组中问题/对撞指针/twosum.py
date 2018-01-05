"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
Leetcode 167
"""
#类似问题Leetcode125，344，345，11
def twoSum(numbers, target):
    #时间复杂度0(nlogn)
    for i in range(len(numbers)):
        num = binarySearch(numbers[i+1:],target-numbers[i])#依次遍历列表，再用二分查找列表剩余元素中是否有target-numbers[i
        index2 = i+num+2
        index1 = i+1
        if num != -1:#
            return index1,index2
    return "not exist index"
def binarySearch(alist,num):
    left = 0
    right = len(alist)-1
    while left <= right:
        mid = (left+right)//2
        if num < alist[mid]:
            right = mid - 1
        elif num==alist[mid]:
            return mid
        else:
            left = mid + 1
    return -1
print(twoSum([2,7,8,9,10,11],21))


def twoSum(numbers, target):#对撞指针
    #时间复杂度0(n)
    l,r = 0,len(numbers)-1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return l+1,r+1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            r -= 1
    return "the input has no solution"
print(twoSum([2,7,11,15,18,19],9))
