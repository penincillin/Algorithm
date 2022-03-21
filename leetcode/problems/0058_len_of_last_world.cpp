/*
 * Length of Last Word. https://leetcode.com/problems/length-of-last-word/
 */


#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int i=0, count=0;
        bool meet_blank = false;
        while(i < s.size()){
            if(s[i] != ' '){
                if (meet_blank){
                    count = 1;
                    meet_blank = false;
                }
                else{
                    count ++;
                }
            }
            else{
                meet_blank = true;
            }
            i++;
        }
        return count;
    }
};

int main(){
    string s = "a    aaa   ";
    Solution sol;
    int res = sol.lengthOfLastWord(s);
    cout << res << "\n";
    return 0;
}
