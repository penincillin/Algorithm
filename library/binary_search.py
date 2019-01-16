import os, sys, shutil

def bin_search_left(l, target):
    start, end = 0, len(l)-1
    while end-start>=1:
        mid = (start+end)//2
        if l[mid]>=target:
            end = mid
        else:
            start = mid+1
    return start

def bin_search_right(l, target):
    start, end = 0, len(l)-1
    while end-start>=1:
        mid = (start+end)//2
        if l[mid]<=target:
            start = mid
        else:
            end = mid-1
    return start


if __name__ == '__main__':

    l = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
    target = 3
    
    idx = bin_search_right(l, target)
    print(idx, l[idx])
