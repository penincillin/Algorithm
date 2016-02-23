#ref:http://www.cnblogs.com/lonelycatcher/archive/2011/07/28/2119123.html

import random as rd

def generateArray(N):
    A = range(0,N)
    rd.shuffle(A)
    return A

def solve1(A):
    #this method use only DP, complexity is O(n^2)
    N = len(A)
    L = [1 for i in xrange(N)]
    prev = [-1 for i in xrange(N)]
    max_l, max_i = 1,0
    for i in xrange(1, N):
        for j in xrange(0, i):
            if A[i]>A[j] and L[j]+1>L[i]:
                L[i] = L[j]+1
                prev[i] = j
        if L[i]>max_l:
            max_l = L[i]
            max_i = i

    print 'res',max_l, A[max_i]
    while(max_i>=0):
        print A[max_i],
        max_i = prev[max_i]
    print
    

def solve2(A):
    #this method use DP and binary search, complexity is O(nlogn)
    N = len(A)
    B = [-1 for i in xrange(N)]
    B[0] = 0
    prev = [-1 for i in xrange(N)]
    max_l, max_i = 1,0
    for i in xrange(1, N):
        start, end = 0, max_l
        while(start < end):
            mid = (start+end)/2
            if A[B[mid]] < A[i]: start = mid+1
            else: end = mid
        B[start] = i
        prev[i] = B[start-1]
        if (start+1)>max_l:
            max_l = start+1
            max_i = i

    print 'res',max_l, A[max_i]
    while(max_i>=0):
        print A[max_i],
        max_i = prev[max_i]
    



if __name__ == '__main__':
    N = 100
    A = generateArray(N)

    print A
    solve1(A)
    solve2(A)
