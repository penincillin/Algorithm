/* 67. Add Binary. https://leetcode.com/problems/add-binary/
 */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        string res;
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        int len = max(a.size(), b.size());
        int exceed = 0;
        for(int i=0; i<len; i++){
            int a_digit=0, b_digit=0;
            if (i<a.size()){
                a_digit = a[i]-'0';
            }
            if (i<b.size()){
                b_digit = b[i]-'0';
            }
            int digit = (exceed + a_digit + b_digit)%2;
            exceed = (exceed + a_digit + b_digit)/2;
            res.push_back(char(digit+'0'));
        }
        if (exceed > 0){
            res.push_back(char(exceed+'0'));
        }
        reverse(res.begin(), res.end());;
        return res;
    }
};


int main(){
    string a="1010", b="1011";
    Solution solution;
    string res = solution.addBinary(a, b);
    cout << res << "\n";
    return 0;
}
