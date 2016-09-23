#include <vector>
#include <iostream>
#include <string>

using namespace std;


class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";
        if(strs.size() == 0){
            return res;
        }
        else{
            int prefix_len = 0;
            for(unsigned i=0; i<strs[0].length(); i++){
                bool flag = true;
                for(unsigned j=1; j<strs.size(); j++){
                    if(strs[j][i] != strs[0][i]){
                        flag = false;
                        break;
                    }
                }
                if(flag){
                    prefix_len++;
                }
                else{
                    break;
                }
            }
            return strs[0].substr(0, prefix_len+1);
        }
    }
};
