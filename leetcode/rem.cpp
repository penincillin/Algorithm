#include<iostream>
#include<string>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        if(p.length()==0) return s == "";
        if(s==""){
            if(p[1] == '*') return isMatch(s, p.substr(2));
            else return false;
        }

        if(p.length()>1 && p[1]=='*'){
            if(isMatch(s, p.substr(2))) 
                return true;
            unsigned end = 0;
            while(p[0]==s[end] || p[0]=='.'){
                if(isMatch(s.substr(++end), p.substr(2)))
                    return true;
                if(end == s.length()){
                    return isMatch("", p.substr(2));
                }
            }
            if(end == 0)
                return isMatch(s, p.substr(2));
            
        }
        else if(p[0] == s[0] || p[0]=='.'){
            return isMatch(s.substr(1), p.substr(1));
        }
        else{
            return false;
        }
        return false;
    }

};

int main(){
    string s[] = {"ab"};
    string p[] = {"a*b"};
    Solution ss;
    for(int i=0; i<1; i++)
        cout << ss.isMatch(s[0], p[0]) << endl;
    return 0;
}
