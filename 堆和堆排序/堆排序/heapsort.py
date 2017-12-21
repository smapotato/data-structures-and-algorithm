def heapsort(arr):
    n = len(arr)
    for i in range((n-2)//2,-1,-1):#索引值
        shiftdown(arr,n,i)#先将n个元素最大堆
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]#交换
        shiftdown(arr,i,0)
    return arr
def shiftdown(arr,n,k):
    while 2*k+1 < n:
        j = 2*k+1
        if j+1<n and arr[j+1] > arr[j]:
            j += 1
        if arr[j] >= arr[k]:
            arr[j],arr[k] = arr[k],arr[j]
            k = j
        else:
            break
print(heapsort([5,92,15,46,35,8,7,24,72]))
