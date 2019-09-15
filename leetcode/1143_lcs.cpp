#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.size();
        int n = text2.size();
        int lens[m+1][n+1];
        for(int i=0; i<m+1; i++){
            for(int j=0; j<n+1; j++){
                lens[i][j] = 0;
            }
        }
        for(int i=0; i<m+1; i++){
            for(int j=0; j<n+1; j++){
                if (i==0 || j==0){
                    lens[i][j] = 0;
                }
                else{
                    if(text1[i-1]==text2[j-1]){
                        lens[i][j] = lens[i-1][j-1]+1;
                    }
                    else{
                        lens[i][j] = max(lens[i-1][j], lens[i][j-1]);
                    }
                }
            }
        }
        return lens[m][n];
    }
};

int main(){
    string text1="abcde", text2="ace";
    //string text1="abc", text2="def";
    Solution solution;
    int res = solution.longestCommonSubsequence(text1, text2);
    cout << res << "\n";
    return 0;
}
