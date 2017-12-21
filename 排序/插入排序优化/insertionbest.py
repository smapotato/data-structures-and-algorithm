def insertionbest(arr):
    for i in range(1,len(arr)):
        copy = arr[i]
        index = i
        while index>0 and arr[index-1]>copy:
            arr[index] = arr[index-1]
            index -= 1
        arr[index]=copy
    return arr
#适用于近乎有序的数据
