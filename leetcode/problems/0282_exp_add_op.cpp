/* 282. Expression Add Operators. https://leetcode.com/problems/expression-add-operators/
 * Part of the idea could be refered to https://leetcode.com/problems/expression-add-operators/solution/. 
 * The key idea is to first consider if there is only "+" and "-" and then take "*" into consideration
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> addOperators(string digits, int target) {
        vector<string> res;
        if (digits.size() == 0){
            return res;
        }
        int cur_value = 0;
        string cur_str = "";
        long prev_num = 0;
        long cur_idx = 0;
        _solve(digits, target, res, cur_str, cur_idx, cur_value, prev_num);
        return res;
    }

    void _solve(string digits, int target, vector<string>& res, string cur_str, int cur_idx, long cur_value, long prev_num){
        if (cur_idx == digits.size()){
            if (cur_value == target){
                res.push_back(cur_str);
                return;
            }
        }
        else{
            for(int i=cur_idx+1; i<=digits.size(); i++){
                string sub_str = digits.substr(cur_idx, i-cur_idx);
                if (i-cur_idx>1 && sub_str[0]=='0'){ // should not appear number like 01
                    break;
                }
                else{
                    long cur_num = stol(sub_str);
                    if (cur_idx==0){ // at the very begining
                        _solve(digits, target, res, sub_str, i, cur_num, cur_num);
                    }
                    else{
                        _solve(digits, target, res, cur_str+"+"+sub_str, i, cur_value+cur_num, cur_num);
                        // -cur_num is important, in calcluating the cur_value, treat both "+" and "-" as "+" by adding "-" to cur_num. In this way, the calculating of "*" can be simplified.
                        _solve(digits, target, res, cur_str+"-"+sub_str, i, cur_value-cur_num, -cur_num);
                        _solve(digits, target, res, cur_str+"*"+sub_str, i, cur_value-prev_num+prev_num*cur_num, prev_num*cur_num);
                    }
                }
            }
        }
    }
};

int main(){
    string digits = "123";
    int target = 6;
    Solution solution;
    vector<string> res = solution.addOperators(digits, target);
    for(int i=0; i<res.size(); i++){
        cout << res[i] << "\n";
    }
    return 0;
}
