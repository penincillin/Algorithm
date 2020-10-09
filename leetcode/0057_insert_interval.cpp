/*
 * Insert Interval, https://leetcode.com/problems/insert-interval/
 * The idea is to find where to insert the interval then merge with the current item and keep looping
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


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
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;    
        int head = 0;
        int insert = false;
        while(head < intervals.size()){
            if(!insert && intervals[head][1] >= newInterval[0]){
                if(newInterval[1] < intervals[head][0]){
                    res.push_back(newInterval);
                    insert = true;
                }
                else{
                    int i0 = min(intervals[head][0], newInterval[0]);
                    int i1 = max(intervals[head][1], newInterval[1]);
                    newInterval[0] = i0;
                    newInterval[1] = i1;
                    head ++;
                }
            }
            else{
                res.push_back(intervals[head]);
                head ++;
            }
        }

        if (! insert){
            res.push_back(newInterval);
        }
        return res;
    }
};

int main(){
    /*
    vector<int> v1{1, 3};
    vector<int> v2{6, 9};
    vector<vector<int>> intervals{v1, v2};
    vector<int> v_n{2, 5};
    */

    vector<int> v1{1, 2};
    vector<int> v2{3, 5};
    vector<int> v3{6, 7};
    vector<int> v4{8, 10};
    vector<int> v5{12, 16};
    vector<vector<int>> intervals{v1, v2, v3, v4, v5};
    vector<int> v_n{4, 8};

    /*
    vector<int> v1{1, 5};
    vector<vector<int>> intervals{v1};
    vector<int> v_n{6, 8};
    */

    Solution sol;
    vector<vector<int>> res = sol.insert(intervals, v_n);
    print_vec(res);
    return 0;
}
