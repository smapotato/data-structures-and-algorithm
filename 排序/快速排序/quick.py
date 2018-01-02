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


def quicksort(arr, left, right):
    # 只有left < right 排序
    if left < right:
        # pivot_index = partition(arr, left, right)
        random_index = random.randint(left, right)
        arr[left], arr[random_index] = arr[random_index], arr[left]
        pivot = arr[left]
        lt = left # arr[left+1...lt] < v
        gt = right + 1 # arr[gt...right] > v
        i = left + 1 # arr[lt+1...i] == v
        while i < gt:
            if arr[i] < pivot:
                arr[i], arr[lt+1] = arr[lt+1], arr[i]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt-1] = arr[gt-1], arr[i]
                gt -= 1
            else:
                i += 1
        arr[left], arr[lt] = arr[lt], arr[left]
        quicksort(arr, left, lt-1)
        quicksort(arr, gt, right)
