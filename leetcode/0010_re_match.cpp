/* Regular Expression Matching, https://leetcode.com/problems/regular-expression-matching/
 * Solving use DP.
 */

#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
using namespace std;

template <typename T>
void print_vec(vector<T> vec){
    for(int i=0; i<vec.size(); i++){
        cout << vec[i] << " ";
    }
    cout << "\n";
}

template <typename T>
void print_vec_II(vector<vector<T>> vec){
    for(int i=0; i<vec.size(); i++){
        for(int j=0; j<vec[i].size(); j++){
            cout << vec[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "------------------\n";
}


class Solution {
public:
    bool isMatch(string s, string p) {
        //p = process_p(p);
        //return solve(s, p, 0, 0);

        return solve_dp(s, p);
    }

    // {{{
    string process_p(string p){
        if (p.length() <= 3){
            return p;
        }
        else{
            string res = p.substr(0, 3);
            for(int i=3; i<p.length(); i++){
                if (i % 2 == 1){
                    char c_1 = res[res.size()-2];
                    char c_2 = res[res.size()-3];
                    //cout << p[i] << " " << p[i-1] << " " << c_2 << " " << c_1 << "\n";
                    if (p[i]=='*' && p[i-1] == c_2 && c_1 == '*'){
                        cout << p[i] << " " << p[i-1] << " " << c_2 << " " << c_1 << "\n";
                        res = res.substr(0, res.size()-1);
                    }
                    else{
                        res += p.substr(i, 1);
                    }
                }
                else{
                    //cout << p.substr(i, 1) << "\n";
                    res += p.substr(i, 1);
                }
            }
            return res;
        }
    }
    // }}}

    bool solve_dp(string s, string p){
        int M = s.length();
        int N = p.length();
        bool res[M+1][N+1];
        memset(res, 0, sizeof(res));
        res[0][0] = 1;
        for(int i=2; i<=N; i++){
            if (p[i-1] == '*'){
                res[0][i] = res[0][i-2];
            }
        }
        for (int i=1; i<=M; i++){
            for(int j=1; j<=N; j++){
                if (p[j-1] == '*'){
                    res[i][j] = res[i][j-2]; // important
                    if (p[j-2] == '.' || p[j-2] == s[i-1]){
                        res[i][j] |= res[i-1][j]; // important, should use res[i-1][j] instead of res[i-1][j-2];
                    }
                }
                else if (p[j-1] == '.' || p[j-1] == s[i-1]) {
                    res[i][j] = res[i-1][j-1];
                }
                else{
                    continue; // do noting
                }
            }
        }
        return res[M][N];
    }

    bool solve(string s, string p, int s_id, int p_id){
        /*
        if (s_id <= s.length() && p_id <= p.length()){
            cout << s.substr(s_id) << " " << p.substr(p_id) << "\n";
        }
        */

        if (s_id >= s.length() && p_id >= p.length()){
            return true;
        }
        else if ( s_id < s.length() && p_id >= p.length() ){
            return false;
        }
        else{
            if (p_id+1 < p.length() && p[p_id+1] == '*'){
                if (s_id >= s.length()){
                    return solve(s, p, s_id, p_id+2);
                }
                else if  (p[p_id] == s[s_id] || p[p_id]=='.'){
                    bool res = solve(s, p, s_id+1, p_id);
                    if (! res){
                        return solve(s, p, s_id, p_id+2);
                    }
                    else{
                        return true;
                    }
                }
                else{
                    return solve(s, p, s_id, p_id+2);
                }
            }
            else{
                if (s_id >= s.length()){
                    return false;
                }
                else{
                    bool cond1 = s[s_id] == p[p_id];
                    bool cond2 = p[p_id] == '.';
                    if (cond1 || cond2){
                        return solve(s, p, s_id+1, p_id+1);
                    }
                    else{
                        return false;
                    }
                }
            }
        }
    }
};


int main(){
    //string s = "", p = "";
    //string s = "ab", p = ".*";
    //string s = "aa", p = "a*";
    //string s = "aab", p = "c*a*b";
    //string s = "ab", p = ".*c";
    //string s = "aaa", p = "ab*a*c*a";
    string s = "aa", p="a*";
    //string s = "a", p = ".*..a*";
    //string s = "aaaaaaaaaaaaab", p = "a*a*a*a*a*a*a*a*a*a*a*c";

    
    Solution sol;
    bool res = sol.isMatch(s, p);
    cout << res << "\n";
    return 0;
}
