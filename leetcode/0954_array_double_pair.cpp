/*
Array of Doubled Pairs, https://leetcode.com/problems/array-of-doubled-pairs/
The key of this problem is to sort the array and check from large to small.
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
private:
    void count_num(vector<int>& arr, unordered_map<int, int>& num_count){
        for(auto num : arr){
            if (num_count.find(num) == num_count.end()){
                num_count[num] = 1;
            }
            else{
                num_count[num] += 1;
            }
        }
    }
public:
    bool canReorderDoubled(vector<int>& arr){
        sort(arr.begin(), arr.end());
        // print_vec(arr);

        unordered_map<int, int> num_count;
        count_num(arr, num_count);
        /*
        for(auto it=num_count.begin(); it!=num_count.end(); it++){
            cout << it->first << " " << it->second << "\n";
        }
        */

        // from tail to head, non-negative first
        int idx = arr.size()-1;
        while(idx-1 >= 0 && arr[idx] >= 0){
            int second = arr[idx], first = second / 2;
            if (num_count[second] > 0){
                bool cond1 = second%2==0; // second itself is even number;
                bool cond2 = num_count.find(first) != num_count.end(); // second/2 exist
                bool cond3 = num_count[first] > 0; // second/2 is not used;
                if (cond1 && cond2 && cond3){
                    num_count[second] -= 1;
                    num_count[first] -= 1;
                    idx -= 1;
                }
                else{
                    // cout << "here-0";
                    return false;
                }
            }
            else{
                idx -= 1;
            }
        }

        // from head to tail, negative number
        idx = 0;
        while(idx+1 < arr.size() && arr[idx] <= 0){
            int second = arr[idx], first = second / 2;
            if (num_count[second] > 0){
                bool cond1 = second%2==0; // second itself is even number;
                bool cond2 = num_count.find(first) != num_count.end(); // second/2 exist
                bool cond3 = num_count[first] > 0; // first is not used;
                if (cond1 && cond2 && cond3){
                    num_count[second] -= 1;
                    num_count[first] -= 1;
                    idx += 1;
                }
                else{
                    return false;
                }
            }
            else{
                idx += 1;
            }
        }

        return true;

    }
};

int main(){
    vector<int> arr;
    arr = {3,1,3,6};
    arr = {2,1,2,6};
    arr = {4,-2,2,-4, 8};

    Solution sol;
    bool res = sol.canReorderDoubled(arr);
    cout << res << "\n";
    return 0;
}
