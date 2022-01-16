/*
Student Attendance Record I: https://leetcode.com/problems/student-attendance-record-i/
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <string>
#include <map>
using namespace std;

class Solution {
public:
    bool checkRecord(string s) {
        int num_a = 0, max_l = 0, count_l = 0;
        for(auto c:s){
            if (c == 'A'){
                num_a += 1;
                count_l = 0;
            }
            else if (c == 'L'){
                count_l += 1;
                max_l = max(count_l, max_l);
            }
            else{
                count_l = 0;
            }
        }
        return num_a<2 && max_l<3;
    }
};

int main(){
    Solution sol;
    string s;
    s = "LLLALL";
    bool res = sol.checkRecord(s);
    cout << res << "\n";
    return 0;
}
