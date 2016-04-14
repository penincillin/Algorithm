#include <iostream>
#include <string>
using namespace std;
class Solution {
public:
    string convert(string s, int numRows) {
        int len = s.size();
        int group_size = numRows>1 ? 2*numRows-2 : 1;
        int group_num = len/group_size + 1*(len%group_size!=0);
        string res = "";
        for(int i=0; i<numRows; i++){
            for(int j=0; j<group_num; j++){
                if(i==0 || i==numRows-1){
                    if(group_size*j+i < len)
                        res += s[group_size*j + i];
                }
                else{
                    if(group_size*j+i < len)
                        res += s[group_size*j + i];
                    if(group_size*j+group_size-i < len)
                        res += s[group_size*j + group_size-i];
                }
            }
        }
        return res;
    }
};
int main(){
    string s = "ABC";
    Solution ss;
    cout << ss.convert(s, 2) << endl;
    return 0;
}
