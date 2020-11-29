 /* Roman to Integer, https://leetcode.com/problems/roman-to-integer/
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
    int RomanToInt(string roman) {
        unordered_map<char, int> map_info({
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000},
        });

        int res=0, prev_num=10000;
        for(int i=0; i<roman.size(); i++){
            int cur = map_info[roman[i]];
            if (cur > prev_num){
                res -= prev_num * 2;
            }
            res += cur;
            prev_num = cur;
        }
        return res;
    }
};


int main(){
    Solution sol;
    string roman = "MCMXCIV";
    int res = sol.RomanToInt(roman);
    cout << res << "\n";
    return 0;
}
