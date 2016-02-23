import random as rd

def binSearch_left(A, target):
    #return value is e, than A[e:]>=target, A[:e]<target
    lo, hi = 0, len(A)
    while lo < hi:
        mid = (lo+hi)/2
        if A[mid]<target: lo = mid+1
        else: hi = mid
    return lo

def binSearch_right(A, target):
    #return value is e, than A[:e]<=target, A[e:]>target
    lo, hi = 0, len(A)
    while lo < hi:
        mid = (lo+hi)/2
        if A[mid]<=target: lo = mid+1
        else: hi = mid
    return lo

if __name__ == '__main__':
    A = [1,2,3,4,5]
    print binSearch_right(A,3)
    print binSearch_left(A,3)

