/*
Longest String Chain, https://leetcode.com/problems/longest-string-chain/
The basic idea is DP. The key of this problem is how to reduce the time complexity given DP framework.
Refer to annotations in solution_02 and solution_01 for more details.
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
#include <array>
#include <queue>
using namespace std;

template<typename T>
void print_array(T A[], int size){
    for(int i=0; i<size; i++){
        cout << A[i] << " ";
    }
    cout << "\n";
}

template <typename T>
void print_vec(vector<T> vec){
    for(auto v:vec){
        cout << v << " ";
    }
    cout << "\n";
}

typedef unordered_map<int, vector<int>> word_info;

class Solution {
private:
    void print_org_words(word_info& len2idxs, vector<string>& words){
        for(int i=1; i<=16; i++){
            auto sub_word_idxs = len2idxs[i];
            if (sub_word_idxs.size() > 0){
                cout << i << ": ";
                for(auto w_id : sub_word_idxs){
                    cout << words[w_id] << " ";
                }
                cout << "\n";
            }
        }
    }

    word_info org_word_by_length(vector<string>& words){
        word_info len2idxs;
        for(int i=1; i<=16; i++){ // max length of word is 16, as specified by the problem
            len2idxs[i] = vector<int>();
        }
        // for(auto word : words){
        for(int i=0; i<words.size(); i++){
            len2idxs[words[i].length()].push_back(i);
        }
        return len2idxs;
    }

    bool is_pred(string word1, string word2){
        int i1 = 0, i2 = 0, num_m = 0; // num_m refers to number of mismatch;
        while(i1 < word1.size() && i2 < word2.size()){
            if (word1[i1] == word2[i2]){
                i1 += 1;
                i2 += 1;
            }
            else{
                i2 += 1;
                num_m += 1;
            }
        }
        return (num_m < 2);
    }

public:
    int longestStrChain(vector<string>& words) {
        return solve_02(words);
    }

    int solve_02(vector<string>& words){
        /*
        Suppose the number of words is N and length of word is S;
        Idea is similar to solve_01. DP is also required. The difference lies in instead of densely checking every pair of possible word. This method only checks word with its possible predecessor via making the predecessor.
        Therefore, the time complexity is O(NS^2)
        */
        word_info len2idxs = org_word_by_length(words);

        unordered_map<string, int> word2idx;
        for(int i=0; i<words.size(); i++){
            word2idx[words[i]] = i;
        }

        const int N = words.size();
        int dp[N];
        for(int i=0; i<N; i++){
            dp[i] = 1;
        }
        int res = 1;

        for(int len=2; len<=16; len++){
            vector<int> idxs = len2idxs[len];
            for(int idx : idxs){
                string word = words[idx];
                for(int j=0; j<word.size(); j++){
                    string pre_word = word.substr(0, j) + word.substr(j+1); // every-possible predecessor word;
                    if (word2idx.find(pre_word) != word2idx.end()){
                        int pre_idx = word2idx[pre_word];
                        dp[idx] = max(dp[idx], dp[pre_idx]+1);
                        res = max(dp[idx], res);
                    }
                }
            }
        }
        return res;
    }

    int solve_01(vector<string> & words){
        /*
        Suppose the number of words is N and length of word is S;
        1. Org the word by length.
        2. Use DP to check the progressively update the results by length of word.
        3. Time complexity: O(SN^2)
        */
        word_info len2idxs = org_word_by_length(words);
        // print_org_words(len2idxs, words);

        const int N = words.size();
        int dp[N];
        for(int i=0; i<N; i++){
            dp[i] = 1;
        }

        int res = 1;
        for(int len=1; len<=15; len++){
            vector<int> idxs1 = len2idxs[len];
            vector<int> idxs2 = len2idxs[len+1];
            for(int idx1 : idxs1){
                string word1 = words[idx1];
                for(int idx2 : idxs2){
                    string word2 = words[idx2];
                    bool test = is_pred(word1, word2);
                    if (is_pred(word1, word2)){
                        dp[idx2] = max(dp[idx1]+1, dp[idx2]);
                        res = max(dp[idx2], res);
                    }
                }
            }
        }
        return res;
    }
};


int main(){
    vector<string> words;
    // words = {"a","b","ba","bca","bda","bdca"};
    words = {"xbc","pcxbcf","xb","cxbc","pcxbc"};
    // words = {"abcd","dbqca"};

    Solution sol;
    int res = sol.longestStrChain(words);
    cout << res << "\n";
    return 0;
}
