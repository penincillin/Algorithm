import os, sys, shutil

def bin_search_left(l, target):
    # return value is i, then a[i:]>=x and a[:i]<x
    start, end = 0, len(l)
    while start<end: 
        mid = (start+end)//2
        if l[mid] < target:
            start = mid+1
        else:
            end = mid
    return start

def bin_search_right(l, target):
    # return value is i, then a[:i]<=x a nd a[i:]>x
    start, end = 0, len(l)
    while start<end: 
        mid = (start+end)//2
        if target < l[mid]:
            end = mid
        else:
            start = mid+1
    return start


if __name__ == '__main__':

    l = [1,2,3,3,3,4,5]
    #l = [5,7,7,8,8,10]
    target = 3 
    
    idx = bin_search_left(l, target)
    print(idx, l[idx])
