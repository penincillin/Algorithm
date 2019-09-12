// refer idea to https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13656/An-O(N)-solution-with-detailed-explanation

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <unordered_map>
using namespace std;


class Solution {
public:
    vector<int> findSubstring(string s, vector<string> &words) {
        vector<int> res;
        if (s.size()==0 || words.size()==0 || words[0].size()==0){
            return res;
        }
        unordered_map<string, int> word_counts;
        for(auto it=words.begin(); it!=words.end(); it++){
            word_counts[*it] += 1;
        }

        int num_word = words.size();
        int len_word = words[0].size();
        int len_s = s.size();
        for(int i=0; i<len_word; i++){
            int head=i;
            int count=0;
            unordered_map<string, int> word_found;
            for(int j=i; j<=len_s-len_word; j+=len_word){
                string substr = s.substr(j, len_word);
                if (word_counts.count(substr)>0){
                    word_found[substr] += 1;
                    count += 1;
                    if (word_found[substr]>word_counts[substr]){
                        while(word_found[substr] > word_counts[substr]){
                            string substr_head = s.substr(head, len_word);
                            word_found[substr_head]--;
                            count--;
                            head += len_word;
                        }
                    }
                    else{
                        if(count == num_word){
                            string substr_head = s.substr(head, len_word);
                            word_found[substr_head]--;
                            count--;
                            res.push_back(head);
                            head += len_word;
                        }
                    }
                }
                else{
                    word_found.clear();
                    count = 0;
                    head = j+len_word;
                }
            }
        }
        return res;
    }

};

int main(){
    Solution solution;
    /*
    string s = "barfoothefoobarman";
    vector<string> words = {"foo", "bar"};
    string s = "wordgoodgoodgoodbestword";
    vector<string> words = {"word","good","best","word"};
    string s="barfoofoobarthefoobarman";
    vector<string> words = {"bar","foo","the"};
    string s = "wordgoodgoodgoodbestword";
    vector<string> words = {"word","good","best","good"};
    */
    string s = "aaaaaaaa";
    vector<string> words = {"aa","aa","aa"};
    vector<int> res = solution.findSubstring(s, words);
    for (auto i=0; i<res.size(); i++){
        cout << res[i] << " ";
    }
    cout << "\n";
    return 0;
}
