import time
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

array = [98,23,45,14,6,67,33,42]
BubbleSort(array)
start_time = time.time()
print(array)
print(time.time() - start_time)