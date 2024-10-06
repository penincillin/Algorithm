/* String to Integer (atoi), https://leetcode.com/problems/string-to-integer-atoi/
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
    int myAtoi(string str) {
        bool neg = false;
        long long res = 0;
        int head = 0, n = str.size();
        const int int_min = -2147483648;
        const int int_max = 2147483647;

        // get all empty first
        while(head < n && str[head]==' '){
            head++;
        }

        // start checking
        if (head < n){
            // check valid number
            if ((str[head]>='0' && str[head]<='9') || str[head]=='+' || str[head]=='-'){
                if (str[head] == '-' || str[head] == '+'){
                    neg = str[head]=='-' ? true : false;
                    head ++;
                }
                while(head < n){
                    if(str[head]>='0' && str[head]<='9'){
                        res = res*10 + str[head]-'0';
                        head ++;
                        if ( neg && -res<int_min ){
                            return int_min;
                        }
                        if (! neg && res>int_max){
                            return int_max;
                        }
                    }
                    else{
                        // when invalid character appears, return current result;
                        return res * (neg ? -1 : 1);
                    }
                }
                return res * (neg ? -1 : 1);
            }
            else{
                return 0;
            }
        }
        else{
            return 0;
        }
    }
};


int main(){
    string str=" -42";
    Solution sol;
    int res = sol.myAtoi(str);
    cout << res << "\n";
    return 0;
}
