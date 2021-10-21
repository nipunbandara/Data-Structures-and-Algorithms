'''

MAX_HEAPIFY(A, i)

    l = LEFT(i)
    r = RIGHT(i)

    if l <= A.heap_size and A[l] > A[i]
        largest = l;
    else
        largest = i;
    
    if r <= A.heap_size and A[r] > A[largest]
        largest = r;
    
    if largest != i
        exchange A[i] with A[largest]
        MAX_HEAPIFY(A, largest)
    
T(n) = O(lgn)


BUILD_MAX_HEAP(A)
    
    A.heap_size = A.length
    for i = [A.length / 2] down to 1
        MAX_HEAPIFY(A, i)


T(n) = n/(2^h+1)O(n)



HEAPSORT(A)

    BUID_MAX_HEAP[A]
    for i = A.length down to 2
        exchange A[1] with A[i]
        A.heap_size = A.heap_size - 1
        MAX_HEAPIFY(A, 1)

T(n) = O(nlogn) 



HEAP_EXTRACT_MAX(A)

    if A.heap_size >= 1
        max - A[1]
        A[1] = A[A.heap_size]
        A.heap_size = A.heap_size - 1
        MAX_HEAPIFY(A, 1)
        return max

T(n) = O(logn)

HEAP_INSERT(A, key)

    A.heap_size = A.heap_size + 1
    i = A.heap_size //assume A[i] = infinity

    while i > 1 and A[PARENT(i)] < key
        A[i] = A[PARENT(i)]
        i = PARENT(i)
    
    A[i] = key


T(n) = O(lgn)


'''