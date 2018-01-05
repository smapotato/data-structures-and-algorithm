from random import randint
import timeit

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
    return alist

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint=partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    rand = randint(first, last) #随机取标定点，以解决近乎有序的列表
    alist[first],alist[rand]=alist[rand],alist[first]
    pivotvalue=alist[first]
    leftmark=first+1
    rightmark=last
    done=False
    while not done:  #双路快排，以解决有大量相同值的列表
        while leftmark<=rightmark and alist[leftmark]<pivotvalue:
            leftmark += 1
        while rightmark>=leftmark and alist[rightmark]>pivotvalue:
            rightmark -= 1
        if leftmark>rightmark:
            done=True
        else:
            alist[leftmark],alist[rightmark]=alist[rightmark],alist[leftmark]
            leftmark += 1
            rightmark -= 1
    alist[first],alist[rightmark]=alist[rightmark],alist[first]
    return rightmark



import random
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
    return alist
def quickSortHelper(alist,left,right):
    if left < right:
        splitpoint = partition(alist,left,right)
        quickSortHelper(alist,left,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,right)
def partition(alist,left,right):
    rand = random.randint(left, right)  # 随机取标定点，以解决近乎有序的列表
    alist[left], alist[rand] = alist[rand], alist[left]
    pivot = alist[left]
    i = left + 1
    j = left #arr[l+1...j] < pivot ; arr[j+1...i) > pivot
    while i <= right:
        if alist[i] < pivot:
            j += 1
            alist[i],alist[j] = alist[j],alist[i]
        i += 1
    alist[j],alist[left] = alist[left],alist[j]
    return j
print(quickSort([2,3,1,23,5,8,9,34,0]))
