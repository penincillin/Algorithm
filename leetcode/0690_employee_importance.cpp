/*
Employee Importance, https://leetcode.com/problems/employee-importance/
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

void print_vec(vector<int> vec){
    for(auto v:vec){
        cout << v << " ";
    }
    cout << "\n";
}

// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
    Employee (int id, int importance, vector<int> subordinates) {
        this->id = id;
        this->importance = importance;
        this->subordinates = subordinates;
    }
};

class Solution {
private:
    unordered_map<int, Employee*> id2em;
public:
    int getImportance(vector<Employee*> employees, int id) {
        // build ID to employee mapping
        for (auto em : employees){
            id2em[em->id] = em;
        }

        int res = 0;
        vector<Employee*> queue;
        queue.push_back(id2em[id]);
        while (queue.size() > 0){
            Employee* top_em = queue[0]; queue.erase(queue.begin());
            res += top_em->importance;
            for(auto subord_id : top_em->subordinates){
                queue.push_back(id2em[subord_id]);
            }
        }
        return res;
    }
};

int main(){
    // Employee em1(0, 1, vector<int>({0,1}));
    Employee em1(1, 5, {2, 3});
    Employee em2{2, 3, {}};
    Employee em3{3, 3, {}};
    vector<Employee*> employees = {&em1, &em2, &em3};
    int id = 1;

    Solution sol;
    cout << sol.getImportance(employees, id) << "\n";
    return 0;
}