def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
    return alist

def quickSortHelper(alist,first,last):
    if first<last:
        ltend,gtstart=partition(alist,first,last)
        quickSortHelper(alist,first,ltend)
        quickSortHelper(alist,gtstart,last)

def partition(alist,first,last):
    rand = randint(first, last) 
    alist[first],alist[rand]=alist[rand],alist[first]
    pivotvalue=alist[first]
    leftmark=first+1
    rightmark=last
    lt,gt,i = first,last+1,first+1
    done=False
    while not done:  #三路快排，解决有大量相同值的列表更快
        if alist[i] < pivotvalue:
            alist[i],alist[lt+1] = alist[lt+1],alist[i]
            lt +=1
            i += 1
        elif alist[i] >pivotvalue:
            alist[i],alist[gt-1] = alist[gt-1],alist[i]
            gt -= 1
        else:
            i += 1
        if i >= gt:
            done = True
    alist[first],alist[lt]=alist[lt],alist[first]
    return lt-1,gt


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
