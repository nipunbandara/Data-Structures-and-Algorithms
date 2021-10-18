A = []
for v in range(4):
    A.append(int(input('Enter a number : ')))
print(A)

def selectionSort(A):
    n = A.length
    for j in range(0, n-1):
        smallest = j
        for i in range(j+1, n):
            if A[i] < A[smallest]:
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]

selectionSort(A)
print('sorted array : ')
print(A)
