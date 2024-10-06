/*
Longest Arithmetic Subsequence of Given Difference; https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
DP
*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <string>
#include <map>
#include <unordered_map>
#include <set>
#include <array>
#include <queue>
using namespace std;

template<typename T>
void print_array(T A[], int size){
    for(int i=0; i<size; i++){
        cout << A[i] << " ";
    }
    cout << "\n";
}

template <typename T>
void print_vec(vector<T> vec){
    for(auto v:vec){
        cout << v << " ";
    }
    cout << "\n";
}

class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        return solve(arr, difference);
    }

    int solve(vector<int>& arr, int difference){
        int diff = difference;
        unordered_map<int, int> dp;
        for(auto num : arr){
            dp[num] = 0;
        }

        int res = 1;
        for(auto num : arr){
            int prev = num - diff;
            if(dp.find(prev) != dp.end()){
                dp[num] = max(dp[num], dp[prev]+1);
                res = max(res, dp[num]);
            }
            else{
                dp[num] = 1;
            }
        }
        return res;
    }
};

int main(){
    vector<int> arr;
    int difference;

    arr = {1,5,7,8,5,3,4,2,1};
    difference = -2;

    Solution sol;
    int res = sol.longestSubsequence(arr, difference);
    cout << res << "\n";
    return 0;
}