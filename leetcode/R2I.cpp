#include <iostream>
#include <string>
#include <map>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        s += 'P'; //P means padding here
        map<char, int> roman_map;
        roman_map['I'] = 1; roman_map['V'] = 5;
        roman_map['X'] = 10; roman_map['L'] = 50;
        roman_map['C'] = 100; roman_map['D'] = 500;
        roman_map['M'] = 1000; roman_map['P'] = 0;

        int res = 0, idx = 0, length = s.length();
        while(idx < length){
            int pre = roman_map[s[idx]];
            int post = roman_map[s[idx+1]];
            if (post>pre){
                res += (post-pre);
                idx += 2;
            }
            else{
                res += pre;
                idx += 1;
            }
        }
        return res;
    }
};

int main(){
    string roman = "IV";
    Solution ss;
    cout << ss.romanToInt(roman) << endl;
    return 0;
}
