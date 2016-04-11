#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int solve1(string s){
        int head=0, res=0;
        int loc[256];
        for(int i=0; i<256; i++) loc[i] = -1;
        for(int tail=0; tail<s.size(); tail++){
            int posi = int(s[tail]);
            if(loc[posi] >= head){
                head = loc[posi] + 1;
            }
            loc[s[tail]] = tail;
            res = max(tail-head+1, res);
        }
        return res;
    }
    int solve2(string s){
       int head=0, tail=0, res=0;
        int loc[256];
        for(int i=0; i<256; i++) loc[i] = -1;
        while(tail<s.size()){
            int posi = int(s[tail]);
            if(loc[posi] >= 0){
                int new_head = loc[posi]+1;
                for(int i=head; i<new_head; i++) loc[s[i]] = -1;
                head = new_head;
                loc[s[head]] = head;
            }
            loc[posi] = tail;
            tail += 1;
            res = max(res, tail-head);
        }
        return res; 
    }
    int lengthOfLongestSubstring(string s) {
        return solve2(s);       
    }
};

int main(){
    string s = "abba";
    Solution ss;
    cout << ss.lengthOfLongestSubstring(s) << endl;
    return 0;
}

/* version 1 is more elegant than version 2, although they are very similar */
