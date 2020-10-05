/*
 * Longest Palindrome: https://leetcode.com/problems/longest-palindromic-substring/submissions/
 * The key idea is to use DP. And the DP target is flag[i][j] which is palindrome or not. Instead of max_len[i][j]
 * BTW, dynamically updating max_len and start can also save the time.
 */

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int len = s.size();
        bool flag[len][len];

        for(int i=0; i<len; i++){
            for(int j=0; j<len; j++){
                if(i >= j){
                    flag[i][j] = true;
                }
                else{
                    flag[i][j] = false;
                }
            }
        }

        int max_len = 0;
        int head = 0;
        // special handling len(s) == 1
        if (s.size() >= 1){
            max_len = 1;
        }

        // length starts from 2.
        // for substring DP, for loop in length & start idx
        for(int l=2; l<=len; l++){
            for(int i=0; i<=len-l; i++){
                int j = i+l-1;
                flag[i][j] = (s[i]==s[j] && flag[i+1][j-1]);
                if (flag[i][j]){
                    if (j+1-i > max_len){
                        max_len = j+1-i;
                        head = i;
                    }
                }
            }
        }

        return s.substr(head, max_len);
    }
};

int main(){
    Solution sol;

    string s = "aaaaa";
    string res = sol.longestPalindrome(s);
    cout << res << "\n";
    return 0;
}
