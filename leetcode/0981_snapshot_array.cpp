/*
1. The most straightforward idea is to model the whole data-strcture as snap_id -> {index -> value}
2. A better solution (in terms of space complexity and set time) is index -> (snap_id -> value). In this way, the problem is totally the same as https://leetcode.com/problems/time-based-key-value-store/
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

typedef unordered_map<int, int> Array;

class SnapshotArray {
private:
    vector<Array> array;
public:
    SnapshotArray(int length) {
        array.push_back(Array());
    }
    
    void set(int index, int val) {
        array[array.size()-1][index] = val;
    }
    
    int snap() {
        Array new_array = array[array.size()-1];
        array.push_back(new_array);
        return array.size()-2;
    }
    
    int get(int index, int snap_id) {
        return array[snap_id][index];
    }
};

int main(){
    SnapshotArray snapshotArr(1);
    snapshotArr.set(0, 15);
    snapshotArr.snap();
    snapshotArr.snap();
    snapshotArr.snap();
    cout << snapshotArr.get(0, 2) << "\n";
    return 0;
}
