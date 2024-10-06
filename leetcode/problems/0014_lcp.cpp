/* Longest Common Prefix, https://leetcode.com/problems/longest-common-prefix/
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
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0 || strs[0].length() == 0){
            return "";
        }
        else{
            string res = "";      
            int N = strs.size();
            int M = strs[0].length();
            for(int i=0; i<M; i++){
                char c = strs[0][i];
                bool success = true;
                for(int j=1; j<N; j++){
                    if (strs[j][i] != c){
                        success = false;
                        break;
                    }
                }
                if (success){
                    res += strs[0].substr(i, 1);
                }
                else{
                    break;
                }
            }
            return res;
        }
    }
};


int main(){
    vector<string> strs;
    strs.push_back("fower");
    strs.push_back("flow");
    strs.push_back("flight");

    Solution sol;
    string res = sol.longestCommonPrefix(strs);
    cout << res << "\n";
    return 0;
}
