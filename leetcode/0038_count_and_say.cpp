/* 38. Count and Say
 */
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

typedef unordered_map<int, string> int2str_map;

class Solution {
public:
    string countAndSay(int n) {
        vector<int> res, old_res;
        old_res.push_back(1);
        res.push_back(1);
        for (int i=2; i<=n; i++){
            res.clear();
            int cur_number = old_res[0];
            int number_count = 1;
            //cout << "old_res size " << old_res.size() << "\n";
            for(int j=1; j<old_res.size(); j++){
                if (old_res[j]==cur_number){
                    number_count += 1;
                }
                else{
                    res.push_back(number_count);
                    res.push_back(cur_number);
                    cur_number = old_res[j];
                    number_count = 1;
                }
            }
            res.push_back(number_count);
            res.push_back(cur_number);
            old_res = res;
        }
        string res_str = "";
        for (int i=0; i<res.size(); i++){
            res_str += to_string(res[i]);
        }
        return res_str;
    }
};

int main(){
    Solution solution;
    for (int i=1; i<30; i++){
        cout << solution.countAndSay(i) << "\n";
        solution.countAndSay(i);
    }
    return 0;
}
