/* using dynamic programming to solve it
 * similar to exe 6.7 in Algorithms */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int len = s.size();
        bool flag[len][len];
        int max_len=-1, head=0;
        for(int i=0; i<len; i++){
            for(int j=0; j<len; j++){
                if(i>=j) flag[i][j]=true;
                else     flag[i][j]=false;
            }
        }
        for(int l=1; l<=len; l++){
            for(int i=0; i<=len-l; i++){
                int j = i+l-1;
                flag[i][j] = ((s[i]==s[j]) && flag[i+1][j-1]);
                if(flag[i][j]){
                    if(l > max_len){
                        head=i;
                        max_len = l;
                    }
                }
            }
        }
        return s.substr(head, max_len);
    }
};

int main(){
    Solution ss;
    string s = "abcbe";
    cout << ss.longestPalindrome(s) << endl;
    return 0;
}
