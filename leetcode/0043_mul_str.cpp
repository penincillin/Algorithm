/* 43. Multiply Strings. The idea is not hard, just follow the rule of multiplication.
 * 
 */

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {
        int len = num1.size() + num2.size();
        int res[len];
        for (int i=0; i<len; i++){
            res[i] = 0;
        }

        for (int i=0; i<num1.size(); i++){
            for(int j=0; j<num2.size(); j++){ 
                int idx = (i + j);
                int i1 = num1[num1.size()-1-i]-'0';
                int i2 = num2[num2.size()-1-j]-'0';
                int value = res[idx] + i1 * i2;
                for (int k = idx; k<len; k++){
                    res[k] = value % 10;
                    int residual = value / 10;
                    if (residual == 0) {
                        break;
                    }
                    else{
                        value = res[k+1] + residual;
                    }
                }
            }
        }

        string res_str = "";
        int i = len-1;
        while (i>=0 && res[i]==0){
            i--;
        }
        if (i < 0){
            return "0";
        }
        for (; i>=0; i--){
            string s(1, char(res[i]+'0'));
            res_str += s;
        }
        return res_str;
    }

};


int main(){
    //Solution sol();
    Solution *ss = new Solution();
    string num1 = "0";
    string num2 = "0";
    string res = ss->multiply(num1, num2);
    cout << res << "\n";
    return 0;
}
