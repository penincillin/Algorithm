 /* Integer to Roman, https://leetcode.com/problems/integer-to-roman/submissions/
 */

#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
using namespace std;

template <typename T>
void print_vec(vector<T> vec){
    for(int i=0; i<vec.size(); i++){
        cout << vec[i] << " ";
    }
    cout << "\n";
}

template <typename T>
void print_vec_II(vector<vector<T>> vec){
    for(int i=0; i<vec.size(); i++){
        for(int j=0; j<vec[i].size(); j++){
            cout << vec[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "------------------\n";
}


class Solution {
public:
    string intToRoman(int num) {
        string map_info[4][10] = {
            {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" },
            {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"},
            {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"},
            {"", "M", "MM", "MMM", "", "", "", "", "", ""},
        };
        vector<string> res;
        for(int i=0; i<4; i++){
            res.push_back(map_info[i][num % 10]);
            num /= 10;
        }
        reverse(res.begin(), res.end());
        string roman = "";
        for(int i=0;  i<res.size(); i++){
            roman += res[i];
        }
        return roman;
    }
};


int main(){
    Solution sol;
    int num = 23;
    string res = sol.intToRoman(num);
    cout << res << "\n";
    return 0;
}
