/*
Minimum Number of Refueling Stops, https://leetcode.com/problems/minimum-number-of-refueling-stops/
There two solutions, the key of first dp solution is how to define the dp target and how to implement it
The second priority-queue solution is greedy.
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
    int solve_dp(int target, int startFuel, vector<vector<int>>& stations) {
        int tank = startFuel;
        int N = stations.size() + 1; // add start
        int dp[N]; // dp[i] means the furthest distances can reach with i stops.
        bool used[N]; // whether the i-th station has been used;
        for(int i=0; i<N; i++){
            dp[i] = -1;
            used[i] = false;
        }
        dp[0] = startFuel;
        int stop = 0;
        while (stop < N-1){
            int max_i = -1;
            for(int i=0; i<stations.size(); i++){
                int dist = stations[i][0], s_fuel = stations[i][1];
                if (!used[i] && dist <= dp[stop]){
                    if (dp[stop]+s_fuel > dp[stop+1]){
                        dp[stop+1] = dp[stop] + s_fuel;
                        if (max_i >= 0){
                            used[max_i] = false; // recover the temporally set station
                        }
                        used[i] = true;
                        max_i = i;
                    }
                }
            }
            stop ++;
            if (dp[stop] >= target){
                return stop;
            }
        }
        return -1;

    }

    int solve_heap(int target, int startFuel, vector<vector<int>>& stations) {
        int tank = startFuel;
        priority_queue<int> pq;
        stations.push_back({target, 0});
        int stop = 0;
        for(auto station : stations){
            int dist = station[0], s_fuel = station[1];
            if (tank-dist >= 0){
                pq.push(s_fuel);
            }
            else{
                while(tank-dist < 0 and pq.size()>0){
                    int max_fuel = pq.top(); pq.pop(); // pop the maximum
                    tank += max_fuel;
                    stop ++;
                }
                if (tank-dist < 0){
                    break;
                }
                else{
                    pq.push(s_fuel);
                }
            }
        }
        return tank-target>=0 ? stop : -1;
    }

public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        if (startFuel >= target){
            return 0;
        }
        else if (stations.size() == 0){
            return -1;
        }
        else{ 
            // return solve_dp(target, startFuel, stations);
            return solve_heap(target, startFuel, stations);
        }
    }
};

int main(){
    int target, startFuel;
    vector<vector<int>> stations;
    // target = 100; startFuel = 30; stations = {{10, 40}, {30, 30}, {70, 30}};
    // target = 100; startFuel = 10; stations = {{10, 60}, {20, 30}, {30, 30}};
    target = 1000; startFuel = 299; stations = {{13,21},{26,115},{100,47},{225,99},{299,141},{444,198},{608,190},{636,157},{647,255},{841,123}};
    // target = 100; startFuel = 1; stations = {{10,100}};

    Solution sol;
    int res = sol.minRefuelStops(target, startFuel, stations);
    cout << res << "\n";
    return 0;
}
