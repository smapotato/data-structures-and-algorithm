def BinarySearch(arr,num):
    l,r = 0, len(arr)-1
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def Binarysearch(arr,num):
    if len(arr) == 0:
        return False
    else :
        mid = len(arr)//2
        if arr[mid] == num:
            return True
        else:
            if num < arr[mid]:
                return Binarysearch(arr[:mid],num)
            else:
                return Binarysearch(arr[mid:],num)
