'''
MATRIX_MULTIPLY(A, B)

    if column[A] != rows[B]
        error "incompatible dimesions"

    else
        for i = 1 to rows[A]
            for j = 1 to columns[B]
                C[i, j] = 0
                for k = 1 to columns[A]
                    C[i, j] = C[i, j] + A[i, k]*B[k, j]
        return C


MATRIX_CHAIN_ORDER(P)

    n = length[P] -1
    for i = 1 to n
        m[i, j] = 0
    for l = 2 to n
        for i = 1 to n-l+1
            j = i+l-1
            m[i, j] = infinity
            for k = i to j-1
                q = m[i, k] + m[k+1, j] + Pi*Pk*Pj
                if q < m[i, j]
                    m[i, j] = q
                    s[i, j] = k
    
    return m, s


'''