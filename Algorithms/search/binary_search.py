A = []
#input array values should be in sorted order

for v in range(4):
    A.append(int(input('Enter a number : ')))
print(A)

x = int(input('Enter the search value : '))

#low = start index
#high = end index
#x = search value

def binary_search(A, low, high, x):
    if high >= low:
        mid = (high + low)//2

        if A[mid] == x:
            return mid
        elif A[mid] > x:
            return binary_search(A, low, mid - 1, x)
        else:
            return binary_search(A, mid + 1, high, x)
        
    else:
        return -1

result = binary_search(A, 0, len(A) - 1, x)

if result != -1:
    print('Element is present at index : ', str(result))
else:
    print('Element is not present at array')