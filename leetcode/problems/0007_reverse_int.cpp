/*  
 * Reverse Integer, https://leetcode.com/problems/reverse-integer/
 * The only concern is to use long long instead of int.  
 */
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        if (x == -2147483648 || x == 0){
            return 0;
        }
        else{
            bool neg = (x < 0);
            if (neg){
                x = x*-1; // change negative to positive
            }
            vector<int> digits;
            while(x > 0){
                digits.push_back(x % 10);
                x /= 10;
            }
            long long res = 0;
            for(int i=0; i<digits.size(); i++){
                long long new_res = res*10 + digits[i];
                if (new_res > 2147483647){
                    return 0;
                }
                else{
                    res = new_res;
                }
            }
            if (neg){
                res *= -1;
            }
            return res;
        }
    }
};

int main(){
    int x = -214;
    Solution sol;
    int res = sol.reverse(x);
    cout << x << "\n";
    cout << res << "\n";
    return 0;
}
