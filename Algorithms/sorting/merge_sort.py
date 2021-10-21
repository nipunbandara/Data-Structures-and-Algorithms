'''
MERGESORT(A,p,r)
    if p < r
        q = (p + r)//2
        MERGESORT(A, p, q)
        MERGESORT(A, q+1, r)
        MERGE(A, p, q, r)


p-start index
q-function point
r-last index

MERGE(A, p, q, r)
    n1 = q-p+1
    n2 = r-q
    creste arrays L[1.. n1 + 1] and R [1.. n2 + 1]
    for i in range(1, n1):
        L[i] = A[p+i-1]

    for j in range(1, n2):
        R[j] = A[q+j]
    L[n+1] = infinity
    R[n+1] = infinity

    i = 1
    j = 1

    for k = p to r
        if L[i] <= R[j]
            A[k] = L[i]
            i = i + 1

        else
            A[k] = R[j]
            j = j + 1


T(n) = O(nlogn)

'''

A = []


# def merge(A, l, q, r):
#     i = 1
#     j = q+1
#     k = 0
#     while(i<=q) and (j<=r) done:
#         k = k + 1
#         if A[i] >= A[j]:
#             TEMP[k] = A[i]
#             i = i + 1
#         else:
#             TEMP[k] = A[j]
#             j = j + 1
#     if j > r:
#         for t in range(0, k-1):
#             A[l + t] = TEMP[t+1]


def mergesort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
