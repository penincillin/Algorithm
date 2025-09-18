/*
Asteroid Collision, https://leetcode.com/problems/asteroid-collision/
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
using namespace std;

template <typename T>
void print_vec(vector<T> vec){
    for(auto v:vec){
        cout << v << " ";
    }
    cout << "\n";
}

class Solution {
private:
    void collide(vector<int> &res){
        // while (res.size() > 1){ // collide only happens when there are more than 1 asteroids
        while (res.size() > 1){
            int num0 = res[res.size()-2];
            int num1 = res[res.size()-1];

            if (num0>0 and num1<0){ // collide only happens when the left one is positive and the right one is negative
                if (num0 > num1*-1){
                    res.pop_back();
                }
                else if (num0 < num1*-1){
                    res[res.size()-2] = num1;
                    res.pop_back();
                }
                else{ // num0 == num1
                    res.pop_back(); res.pop_back(); // pop the last two;
                }
            }
            else{
                return;
            }
        }
    }

public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> res;
        int idx = 0;
        for(auto ast : asteroids){
            res.push_back(ast); // add the new item first
            collide(res);
        }
        return res;
    }
};
   

int main(){
    vector<int> asteroids;
    // asteroids = {5,-5};
    asteroids = {-2, -1, -3, 1, -10, 1, -1, 10};
    Solution sol;
    vector<int> res = sol.asteroidCollision(asteroids);
    print_vec(res);
    return 0;
}