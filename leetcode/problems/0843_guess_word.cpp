/*
Guess the Word, https://leetcode.com/problems/guess-the-word/
Refer to: https://leetcode.com/problems/guess-the-word/discuss/133862/Random-Guess-and-Minimax-Guess-with-Comparison
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

class Master {
private:
    string secret;
public:
    Master(string secret): secret(secret) {}
    int guess(string word){
        int res = 0;
        for(int i=0; i<6; i++){
            if (secret[i] == word[i]){
                res += 1;
            }
        }
        return res;
    }
 };

class Solution {
private:
    int get_num_match(string word, string cand){
        int res = 0;
        for(int i=0; i<6; i++){
            if (word[i] == cand[i]){
                res += 1;
            }
        }
        return res;
    }
public:
    void findSecretWord(vector<string>& wordlist, Master& master) {
        solve(wordlist, master);
    }

    void solve(vector<string>& wordlist, Master& master){
        while(true){
            int count[6][26] = {0};
            for (auto word : wordlist){
                for(int i=0; i<6; i++){
                    count[i][word[i]-'a'] += 1;
                }
            }

            int max_score = 0;
            string guess = "";
            for (auto word : wordlist){
                int score = 0;
                for(int i=0; i<6; i++){
                    score += count[i][word[i]-'a'];
                }
                if (score > max_score){
                    max_score = score;
                    guess = word;
                }
            }

            int num_match = master.guess(guess);
            cout << "guess: " << guess << "; num_match: " << num_match << "\n";
            if (num_match == 6){
                break;
            }
            else{
                vector<string> cands;
                cout << "cands: ";
                for(auto cand : wordlist){
                    if (get_num_match(cand, guess) == num_match && cand != guess){
                        cout << cand << " ";
                        cands.push_back(cand);
                    }
                }
                wordlist = cands;
                cout << "\n";
                cout << "------------------------------\n";
            }
        }
    }
    
    void solve_linear(vector<string>& wordlist, Master& master){
        vector<string> cands = wordlist;
        while (cands.size() > 0){
            string word = *(cands.end()-1);
            cands.pop_back();
            // string word = cands[0];
            int num_match = master.guess(word);
            cout << "select: " << word << "; num_match: " << num_match << "\n";
            if (num_match == 6){
                break;
            }
            else{
                vector<string> new_cands;
                cout << "new_cands: ";
                for(auto cand : cands){
                    if (get_num_match(cand, word) == num_match){
                        cout << cand << " ";
                        new_cands.push_back(cand);
                    }
                }
                cout << "\n";
            }
            cout << "------------------------------\n";
        }
    }
};

int main(){
    string secret; vector<string> wordlist;

    secret = "hbaczn";
    wordlist = {"gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"};

    assert (find(wordlist.begin(), wordlist.end(), secret) != wordlist.end());
    Master master(secret);
    Solution sol;
    sol.findSecretWord(wordlist, master);
    return 0;
}
