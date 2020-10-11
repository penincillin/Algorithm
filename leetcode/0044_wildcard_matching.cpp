/*
 * Leetcode 44, https://leetcode.com/problems/wildcard-matching/
 * Use recursive will time-exceed. Use DP also requires carefully design.
 * Refer to https://www.cnblogs.com/grandyang/p/4401196.html for O(n) solving.
 */

#include <iostream>
#include <string>
#include <algorithm>
#include <assert.h> 
using namespace std;

class Solution {
public:
    bool empty_s(string p){
        if (p.size() == 0){
            return true;
        }
        else{
            for (int i=0; i<p.size(); i++){
                if (p[i] != '*'){
                    return false;
                }
            }
            return true;
        }
    }

    bool check(string s, string p, int i_s, int i_p){
        //assert (i_s < s.size());    
        //assert (i_p < p.size());    
        if (p[i_p] != '*'){
            bool value = p[i_p]==s[i_s] | p[i_p]=='?';
            return value;
        }
        else{
            return true;
        }
    }
    
    bool solve_dp(string s, string p){
        int size_s = s.size();
        int size_p = p.size();
     
        // s and p are both not empty
        // init res first
        bool res[size_s+1][size_p+1];

        // [0, 0] should be true
        res[0][0] = true;
        for(int i=1; i<size_s+1; i++){
            res[i][0] = false;
        }
        for(int j=1; j<size_p+1; j++){
            res[0][j] = (p[j-1]=='*') & res[0][j-1];
        }

        for (int i=1; i<size_s+1; i++){
            for(int j=1; j<size_p+1; j++){

                if (p[j-1] == '*'){
                    res[i][j] = (res[i][j-1] || res[i-1][j-1] || res[i-1][j]);
                }
                else{
                    res[i][j] = (s[i-1]==p[j-1] || p[j-1]=='?') && res[i-1][j-1];
                }

            }
        }
        return res[size_s][size_p];
    }

    bool isMatch(string s, string p) {
        return solve_dp(s, p);
    }
};

int main(){

    int i = 0;
    int j = i++;
    int k = ++i;
    cout << i << " " << j << " " << k << "\n";

    return 0;
    Solution sol;

    //string s = "a";
    //string p = "a*";

    //string s = "mississippi";
    //string p = "m??*ss*?i*pi";

    //string s = "aa";
    //string p = "*";
    

    /*
    string s = "sissippi";
    string p = "*ss*?i*pi";

    for (int i=0; i<s.size(); i++){
        for(int j=0; j<p.size(); j++){
            sol.isMatch(s.substr(0, i), p.substr(0, j));
        }
    }
    return 0;
    */

    //string s = "aab";
    //string p = "c*a*b";

    //string s = "acdc";
    //string p = "a*c?";

    //string s = "babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab";
    //string p = "***bba**a*bbba**aab**b";
    //

    // string s = "siss";
    // string p = "*s*?";
    
    //string s = "aaaaabbaabbabaaaaaaaababababaabbabbbbbbbaabaaaaaaababbbaaabbaaaaabbbaaababbbbbbbaabbbbbabbbbbbbbababbaaaabbbaababaaabbaaabbaabbbaaabaababaabbbaabaabbbbaabababaababaababbaaabaababaaabaaaababbabbabbbbaaabbb";
    //string p = "bb*aa**aa**a**bb*babb*b**bbb**aa**aab*aba******aaab***a*ab***a*****aa**a*a*b**b***bbb*ab********ab*babb*";

    string s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    string p = "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*";

    s = "";
    p = "";

    bool res = sol.isMatch(s, p);
    cout << "res " << res << "\n";
    return 0;
}
