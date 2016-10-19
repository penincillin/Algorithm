# implementation of edit distance algorithm
import os, sys, shutil

def edit_distance(s1, s2):
    edit = [[0]*(len(s2)+1) for i in xrange(len(s1)+1)]
    for i in range(len(s1)+1): edit[i][0] = i
    for j in range(len(s2)+1): edit[0][j] = j
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            edit[i][j] = min(edit[i-1][j]+1, \
                    min(edit[i][j-1]+1, edit[i-1][j-1]+(s1[i-1]!=s2[j-1])))
    return edit[len(s1)][len(s2)]


if __name__ == '__main__':
    s1 = 'abcde'
    s2 = 'abcefd'
    print edit_distance(s1, s2)
