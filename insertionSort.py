A = [99,55,4,66,28,31,36,52,38,72]

def insertionSort(A):
    for i in range(1, len(A)):
        x = A[i]
        j = i -1 
        while j >= 0 and x < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = x
        
insertionSort(A)
print(A)