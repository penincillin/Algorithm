/*
 * Time Based Key-Value Store, https://leetcode.com/problems/time-based-key-value-store/
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

class Sample{
private:
    vector<int> timestamps;
    unordered_map<int, string> time2value;
    int get_idx(int query){
        int start = 0, end = timestamps.size();
        while (start < end){
            int mid = (start+end)/2;
            if (timestamps[mid] <= query){
                start = mid+1;
            }
            else{
                end = mid;
            }
        }
        return start;
    }

public:
    Sample() {}
    Sample(string value, int tm){
        timestamps.push_back(tm);
        time2value[tm] = value;
    }

    void set(string value, int tm){
        time2value[tm] = value;
        int idx = get_idx(tm);
        timestamps.insert(timestamps.begin()+idx, tm);
    }

    string get(int tm){
        int idx = get_idx(tm);
        if (idx == 0){
            return "";
        }
        else{
            return time2value[timestamps[idx-1]];
        }
    }
};

class TimeMap {
private:
    unordered_map<string, Sample> map;

public:
    TimeMap() {}
    
    void set(string key, string value, int tm) {
        if (map.find(key) != map.end()){
            map[key].set(value, tm);
        }
        else{
            Sample sample(value, tm);
            map[key] = sample;
        }
    }
    
    string get(string key, int tm) {
        if (map.find(key) != map.end()){
            return map[key].get(tm);
        }
        else{
            return "";
        }
    }
};


int main(){
    TimeMap timeMap;
    timeMap.set("foo", "bar", 1);
    timeMap.set("foo", "bar2", 4);

    cout << timeMap.get("foo", 1) << "\n";
    cout << timeMap.get("foo", 5) << "\n";

    timeMap.set("foo", "bar3", 1);
    cout << timeMap.get("foo", 1) << "\n";
    return 0;
}
