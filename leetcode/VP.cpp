#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int check_match(char c1, char c2){
        if(c2 == '(' || c2 == '[' || c2 == '{'){
            return 1;
        }
        else{
            if(c1=='(' && c2==')') return 2;
            if(c1=='[' && c2==']') return 2;
            if(c1=='{' && c2=='}') return 2;
        }
        return 0;
    }
    bool isValid(string s) {
        char strs[s.length()];
        int head = -1;
        for(unsigned i=0; i<s.length(); i++){
            if(head==-1){
                strs[head+1] = s[i];
                head++;
            }
            else{
                int match = check_match(strs[head], s[i]);
                if(match == 0){
                    break;
                }
                else{
                    if(match == 1){
                        strs[head+1] = s[i];
                        head++;
                    }
                    else{
                        head--;
                    }
                }
            }
        }
        return (head==-1);
    }
};

int main(){
    string s = "[()]";
    Solution ss;
    cout << ss.isValid(s) << endl;
    return 0;
}
