/*
 *  Longest Palindromic Subsequence, https://leetcode.com/problems/longest-palindromic-subsequence/
 *  Classical DP problem. use O(n^2) time and O(N^2) space.
 *  However, if you check carefully the whole state transition, then you will find that only O(2n) space is required.
 *  To understand how to write this code, you need to draw the table of change of l, k
 */

#include <iostream>
#include <string>
#include <stdio.h>
#include <string.h>
using namespace std;

class Solution {
public:
    int longestPalindromeSubseq_classical(string s){
        int len = s.size();
        if (len == 0) return 0;

        int max_len[len][len];
        memset(max_len, 0, sizeof(max_len[0][0]) * len * len);

        for(int i=0; i<len; i++){
            max_len[i][i] = 1;
        }
        for(int l=2; l<=len; l++){
            for(int i=0; i<len-l+1 ; i++){
                int j = i+l-1;
                max_len[i][j] = max(max_len[i+1][j], max_len[i][j-1]);
                max_len[i][j] = max(max_len[i][j], 2*(s[i]==s[j]) + max_len[i+1][j-1]);
            }
        }
        return max_len[0][len-1];
    }

    int longestPalindromeSubseq_o2n(string s){
        // To understand this faster version
        int len = s.size();
        if (len == 0) return 0;

        int max_len[2][len];
        memset(max_len, 0, sizeof(max_len[0][0]) * len * 2);

        for(int l=0; l<len; l++){ // length
            for(int k=0; k<len-l ; k++){ // start
                int i = l;
                int j = k;
                if (l == 0){
                    max_len[i%2][j] = 1;
                }
                else{
                    max_len[i%2][j] = max(max_len[(i-1)%2][j], max_len[(i-1)%2][j+1]);
                    max_len[i%2][j] = max(max_len[i%2][j], 2*(s[k]==s[k+l]) + max_len[i%2][j+1]);
                }
            }
        }
        return max_len[(len-1)%2][0];
    }
};

int main(){
    Solution sol;
    string s = "bddb";
    int res =sol.longestPalindromeSubseq(s);
    cout << res << "\n";
    return 0;
}
