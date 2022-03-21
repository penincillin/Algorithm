/*
Number of Matching Subsequences, https://leetcode.com/problems/number-of-matching-subsequences/
The key idea is similar to implement trie. The key difference is trie handling substring while this problem handling sub-sequence.
As it is subsequence, therefore, each node only contains the smallest valid index for each character.
Another key is to traverse from tail to head.
*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <string>
#include <map>
#include <unordered_map>
#include <set>
using namespace std;

template<typename T>
void print_array(T A[], int size){
    for(int i=0; i<size; i++){
        cout << A[i] << " ";
    }
    cout << "\n";
}

class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        const int N = s.length();
        int map[26];
        for(int i=0; i<26; i++){
            map[i] = -1;
        }

        int trie_dict[N+1][26];
        for(int i=N-1; i>=0; i--){ // from tail to head
            char c = s[i];
            copy(map, map+26, trie_dict[i+1]);
            map[c-'a'] = i;
        }
        copy(map, map+26, trie_dict[0]);

        int res = 0;
        for(auto word : words){
            int idx = -1;
            bool succeed = true;
            for(auto c : word){
                int next_idx = trie_dict[idx+1][c-'a'];
                if (next_idx >= 0){
                    idx = next_idx;
                }
                else{
                    succeed = false;
                    break;
                }
            }
            if (succeed){
                res += 1;
            }
        }
        return res;
    }
};

int main(){
    string s; vector<string> words;
    // s = "abcde"; words = {"a","bb","acd","ace"};
    s = "dsahjpjauf"; words = {"ahjpjau","ja","ahbwzgqnuk","tnmlanowax"};
    Solution sol;
    int res = sol.numMatchingSubseq(s, words);
    cout << res << "\n";
    return 0;
}