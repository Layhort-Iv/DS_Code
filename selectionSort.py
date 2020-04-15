Arr = [99,55,4,66,28,31,36,52,38,72]

def selectionSort(Arr):
    for i in range(len(Arr)):
        min_value = i
        for j in range(i+1, len(Arr)):
            if Arr[min_value] > Arr[j]:
                min_value = j
        Arr[i], Arr[min_value] = Arr[min_value], Arr[i]


selectionSort(Arr)
# for i in range(len(Arr)):
#     print(Arr[i])
print(Arr)

