/* 
 * ZigZag Conversion, https://leetcode.com/problems/zigzag-conversion/
 * Instead of using brutal force method, write 0 to n-1 (length of string), then check each row. the law is easy to be revealed.
 */

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        string res = "";
        int gap = (numRows-1) * 2;
        int len = s.size();
        for(int i=0; i<numRows; i++){
            int g[2];
            g[0] = (numRows-1-i) * 2;
            g[1] = gap - g[0];
            int head = i;
            int num = 0;
            while(head < len){
                res += s[head];
                if (g[num%2] == 0){
                    num ++;
                    // make sure head at least move forward by 1, this is special handling s.size() == 1
                    head += max(g[num%2], 1);
                }
                else{
                    head += g[num%2];
                    num ++;
                }
            }
        }
        return res;
    }
};

int main(){
    Solution sol;
    string s = "A";
    cout << "length: " << s.size() << "\n";
    int n = 2;
    string res = sol.convert(s, n);
    cout << res << "\n";
    return 0;
}
