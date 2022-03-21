/*
 * Group ANagrams: https://leetcode.com/problems/group-anagrams/solution/
 * Hash using unordered_map
 */

#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> str_map;

        for(int i=0; i<strs.size(); i++){
            string key = strs[i];
            sort(key.begin(), key.end());
            if (str_map.find(key) != str_map.end()){
                str_map[key].push_back(strs[i]);
            }
            else{
                vector<string> node;
                node.push_back(strs[i]);
                str_map[key] = node;
            }
        }

        vector<vector<string>> res;
        for (auto it=str_map.begin(); it!=str_map.end(); it++){
            res.push_back(it->second);
        }
        return res;
    }
};


int main(){
    Solution sol;
    
    vector<string> strs{"eat", "tea", "tan", "ate", "nat", "bat"};

    vector<vector<string>> res = sol.groupAnagrams(strs);
    for(int i=0; i<res.size(); i++){
        for(int j=0; j<res[i].size(); j++){
            cout << res[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
