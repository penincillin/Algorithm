/* 32. Longest Valid Parentheses. https://leetcode.com/problems/longest-valid-parentheses/
 * The idea is basically use num_left to simulate a stack, the tmp_values[num_left] means when stack point comes to num_left, the longest parenthese is ?
*/

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
       int longestValidParentheses(string s) {
        if (s.size() == 0){
            return 0;
        }
        int num_left = 0, num_right=0;
        int last_update = -1;
        int res = 0;
        int tmp_values[s.size()];
        for (int i=0; i<s.size(); i++){
            tmp_values[i] = 0;
        }
        for(int i=0; i<s.size(); i++){
            if (s[i] == '('){
                num_left += 1;
            }
            else{ // s[i] == ')'
                if (num_left>0){
                    num_left -= 1;
                    tmp_values[num_left] += 1;
                    if (last_update == num_left+1){
                        tmp_values[num_left] += tmp_values[num_left+1];
                        tmp_values[num_left+1] = 0;
                    }
                    last_update = num_left;
                    res = max(res, tmp_values[num_left]);
                }
                else{
                    tmp_values[num_left] = 0;
                }
            }
        }
        return res*2;
    }

};


int main(){
    //string s = "(()())";
    //string s = "()(()";
    //string s = "()(())";
    //string s = "((()))())";
    //string s = ")()())()()(";
    //string s = ")(((((()())()()))()(()))(";
    //string s = "(((())(()))((())(((((((()))())((((())())(()())))))))))((()((()(()(()()((()()()(()()()))(()()(()(())())))()())()(((((";
    string s = "(((())(()))((())(((((((()))())((((())())(()())))))))))";
    Solution solution;
    unsigned long long res = solution.longestValidParentheses(s);
    cout << res << "\n";
    return 0;
}
