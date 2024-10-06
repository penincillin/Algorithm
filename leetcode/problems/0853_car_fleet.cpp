/*
Car Fleet, https://leetcode.com/problems/car-fleet/
See the detailed annotation for idea.
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

typedef array<int, 2> Info;

bool surpass(Info info0, Info info1, int target){
    long p0=info0[0], v0=info0[1], p1=info1[0], v1=info1[1];
    return (target-p0)*(v1-v0) >= (p0-p1)*v0;
}

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        /*
        1. Sort the (position, speed) pair by the position. for easy coding, sort from tail to head.
        */
        vector<Info> info_all;
        for(int i=0; i<position.size(); i++){
            info_all.push_back({position[i], speed[i]});
        }
        sort(info_all.begin(), info_all.end());
        reverse(info_all.begin(), info_all.end());

        /*
        Considering c0=(p0, v0), c1=(p1, v1) (p0 is ahead of p1). It is easy to check whether c0,c1 can be merged.
        Now consider we have one additional car c2, (c2, c1, c0). if c1, c0 never meets, then s0 solely forms a fleet and we no need to consider it.
        if c1,c0 can be merged, then it is equivalent to consider (c2, c0), as c1 is merged into c0.
        The thing to pay attention is that, whether the c2 and c3 can be merged first influence the results? The answer is no.
        Suppose we only consider c2 and c0. If c2 and c0 cannot be merged, then merging with c1 will only slow down c2, then c2 can never been merged with c0.
        If c2 and c0 can be merged, if c2 and c1 is merged, then as we know c1 is merged with c0, then c2 can still be merged.
        The key of this problem is whether the c0, c1 can be merged or not, the c0 will not be affected.
        In another word, the car will never be affected by the following car.
        */
        int pop_out = 0;
        auto info_ptr = info_all.begin();
        while(info_ptr != info_all.end()-1){
            Info info0 = *(info_ptr); // c0
            Info info1 = *(info_ptr+1); // c1
            bool can_surpass = surpass(info0, info1, target);
            if (can_surpass){
                *(info_ptr+1) = *(info_ptr);  // merge c1 into c0
                info_ptr += 1;
            }
            else{ 
                // c0 and c1 cannot be merged, then c0 solely forms a fleet and should not be considered again.
                info_ptr += 1;
                pop_out += 1;
            }
        }
        return pop_out + 1; // it should be pop_out + info_all.length() here. However, the info_all.length() will always be 1, so we just write down 1 here.
    }

    int carFleet_erase(int target, vector<int>& position, vector<int>& speed) {
        /*
        The algorithm is totally the same as the above one, the only difference is the implementation.
        This version uses the more natural way of vector, which runs relative slow due to frequently erase operation.
        Refer to the above implementation for idea.
        */
        vector<Info> info_all;
        for(int i=0; i<position.size(); i++){
            info_all.push_back({position[i], speed[i]});
        }
        sort(info_all.begin(), info_all.end());
        reverse(info_all.begin(), info_all.end());

        int pop_out = 0;
        while(info_all.size() > 1){
            Info info0 = info_all[0];
            Info info1 = info_all[1];
            bool can_surpass = surpass(info0, info1, target);
            if (can_surpass){
                info_all[1] = info_all[0];
                info_all.erase(info_all.begin());
            }
            else{
                info_all.erase(info_all.begin());
                pop_out += 1;
            }
        }        
        return pop_out + 1;
    }
};

int main(){
    int target;
    vector<int> position, speed;
    // target = 12; position = {10,8,0,5,3}; speed = {2,4,1,1,3};
    // target = 10; position = {3}; speed = {3};
    // target = 100; position = {0,2,4}; speed = {4,2,1};
    target = 10, position = {0,4,2}; speed = {2,1,3};



    Solution sol;
    int res = sol.carFleet(target, position, speed);
    cout << res << "\n";
    return 0;
}
