#You are given an integer array A. 
#You have to find the second largest element/value in the array or report that no such element exists.



def second_largest(A):
    largest = float('-inf')
    secondlargest = float('-inf')

    for i in range(len(A)):
        if A[i] > largest:
            secondlargest = largest
            largest = A[i]
        elif A[i] > secondlargest and A[i] != largest:
            secondlargest = A[i]

    if secondlargest != float('-inf'):
        return secondlargest
    else:
        return -1



A = [2, 1, 2]
print(second_largest(A))