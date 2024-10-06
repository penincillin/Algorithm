/*
 * Merge Intervals, https://leetcode.com/problems/merge-intervals/
 * The idea is easy, sorting the list by the begining.
 * The key to speed-up is to use vector<int> & instead of vector<int>
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


bool cmp(vector<int> & v1, vector<int> & v2){ // important here, use vector<int> & instead of vector<int> &
    return v1[0] < v2[0];
}

template <typename T>
void print_vec(vector<vector<T>> vec){
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
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;   
        if (intervals.size() == 0){
            return res;
        }
        
        // sort with the first one
        sort(intervals.begin(), intervals.end(), cmp);

        res.push_back(intervals[0]);
        int head = 0;
        for(int i=1; i<intervals.size(); i++){
            if (intervals[i][0] <= res[head][1]){
                res[head][1] = max(intervals[i][1], res[head][1]);
            }
            else{
                res.push_back(intervals[i]);
                head++;
            }
        }
        return res;
    }
};


int main(){

    vector<int> v1{1, 4};
    //vector<int> v2{4, 5};
    vector<vector<int>> intervals{v1};
    //vector<vector<int>> intervals{v1, v2};

    Solution sol;
    vector<vector<int>> res = sol.merge(intervals);
    print_vec<int>(res);

    return 0;
}
