A = []
for v in range(7):
    A.append(input("Enter a number : "))
    print(A)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i +1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i+1


def quicksort(A, p, r):
    if p<r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

quicksort(A, 0, len(A) - 1)
print('sorted array : ')
for i in range(len(A)):
    print(A[i])