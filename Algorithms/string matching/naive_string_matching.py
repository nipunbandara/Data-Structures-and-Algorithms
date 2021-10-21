'''
Naive_String_Matching(T, P)

    n = T.length
    m = P.length
    for s = 0 to n - m
        if P[1..m] == T[s+1 .. s+m]
            print("pattern occurs with shift ", s)


worst case
    T(n) = O((n-m+1)m)
    number of comparisons =  ((n-m+1)m)

Best case
    T(n) = O(n-m+1)
    number of comparisons = (n-m+1)

'''