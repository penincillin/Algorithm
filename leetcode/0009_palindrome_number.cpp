/*
 * Palindrome Number, https://leetcode.com/problems/palindrome-number/
 */

#include <iostream>
#include <string>
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
    bool isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        else if (x == 0){
            return true;
        }
        else{
            vector<int> digits;
            while(x > 0){
                digits.push_back(x % 10);
                x /= 10;
            }
            int head=0, tail=digits.size()-1;
            while(head <= tail){
                if (digits[head] != digits[tail]){
                    return false;
                }
                else{
                    head ++;
                    tail --;
                }
            }
            return true;
        }
    }
};


int main(){
    int x = 0;
    Solution sol;
    bool res = sol.isPalindrome(x);
    cout << res << "\n";
    return 0;
}
