/*
Decode String, https://leetcode.com/problems/decode-string/
The recursive idea is straightforward. The iterative idea uses two stacks.
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
private:
    string multiple_str(string str, int times){
        string res = "";
        for(int i=0; i<times; i++){
            res += str;
        }
        return res;
    }
public:
    string decodeString(string s) {
        string tmp_s = s;
        return solve_stack(s);
    }

    string solve_stack(string &s){
        int count = 0;
        string str = "";
        vector<int> c_stack;
        vector<string> s_stack;
        for (auto c: s){
            if (c == '['){
                c_stack.push_back(count);
                s_stack.push_back(str);
                str = "";
                count = 0;
            }
            else if (c == ']'){
                int prev_c = c_stack.back(); c_stack.pop_back(); // pop
                string prev_s = s_stack.back(); s_stack.pop_back(); // pop
                str = prev_s + multiple_str(str, prev_c);
            }
            else if (c>='0' and c<='9'){
                count = count*10 + (c-'0');
            }
            else{ // English digits
                str += c;
            }
        }
        return str;
    }

    string solve_recursive(string &s){
        string res = "";
        int count = 0;
        while(s.size()>0){
            if (s[0] == '['){
                s = s.substr(1);
                string mid_res = solve_recursive(s);
                res += multiple_str(mid_res, count);
                count = 0;
            }
            else if (s[0] == ']'){
                s = s.substr(1);
                return res;
            }
            else if (s[0]>='0' and s[0]<='9'){
                count = count*10 + int(s[0]-'0');
                s = s.substr(1);
            }
            else{ // English letters
                res += s[0];
                s = s.substr(1);
            }
        }
        return res;
    }
};

int main(){
    Solution sol;
    string s;
    // s = "abcd";
    s = "3[2[a]]";
    // s = "2[3[a]]";
    // s = "3[2[c]b1[a]]";
    // s = "3[a]2[bc]";
    /*
    s = "2[j]e1[f]"
    s = "2[y]pq4[2[j]e1[f]]"
    s = "2[2[y]pq4[2[j]e1[f]]]"
    s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    s = "2[abc]3[cd]ef"
    s = "c3[b2[a]]"
    s = "c3[2[a]]"
    s = "3[acb]"
    s = "3[a2[c]]"
    */

    string res = sol.decodeString(s);
    cout << res << "\n";
    return 0;
}
