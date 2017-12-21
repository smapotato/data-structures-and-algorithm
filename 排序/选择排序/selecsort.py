def sort(a):
    for i in range(len(a)-1):
        min_index = i
        for j in range(i+1,len(a)):
            if a[min_index]>a[j]:
                min_index = j
        a[min_index],a[i] = a[i],a[min_index]
    return a
print(sort([5,4,3,0,2,1]))
O(n^2)
