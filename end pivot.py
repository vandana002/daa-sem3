def partition(A, start, end):

    pivot = A[end] 
    pIndex = start 

    for i in range(start, len(A)):
        if A[i] < pivot:
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex += 1
    A[pIndex], A[end] = A[end], A[pIndex]

    return pIndex

def quickSort(A, start, end):
    if start >=end:
        return
    else:
        pIndex = partition(A, start, end)
        quickSort(A, start, pIndex - 1)
        quickSort(A, pIndex + 1, end)


if __name__ == '__main__':
    
    A = [7,2,1,6,8,5,3,4]
    start = 0
    end = len(A) - 1
    print("Unsorted Array: ",A)
    quickSort(A, start, end)
    print("Sorted Array: ",A)
