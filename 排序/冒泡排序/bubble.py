def bubblesort(arr):
    for passnum in range(len(arr) - 1, 0, -1):
        for i in range(passnum):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr



def shortbubblesort(arr):  # 对于已排序的列表更快
    exchanges = True
    passnum = len(arr) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if arr[i] > arr[i + 1]:
                exchanges = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        passnum -= 1
