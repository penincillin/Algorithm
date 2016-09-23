#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        string roman[4][10] = { {"","I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"},
                             {"","X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"},
                             {"","C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"},
                             {"", "M", "MM", "MMM"}};
        vector<string> mid_str;
        for(int i=0; i<4; i++){
            mid_str.push_back(roman[i][num%10]);
            num /= 10;
        }
        string res = "";
        for(int i=3; i>=0; i--){
            res += mid_str[i];
        }
        return res;
    }
};

int main(){
    Solution ss;
    int input = 4;
    cout << ss.intToRoman(input) << endl;
    return 0;
}
