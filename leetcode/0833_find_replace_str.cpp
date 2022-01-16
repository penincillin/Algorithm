/*
Find And Replace in String, https://leetcode.com/problems/find-and-replace-in-string/

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

template <typename T>
void print_vec(vector<T> vec){
    for(auto v:vec){
        cout << v << " ";
    }
    cout << "\n";
}

template<typename T>
void print_array(T A[], int size){
    for(int i=0; i<size; i++){
        cout << A[i] << " ";
    }
    cout << "\n";
}

struct Query{
    int idx;
    string source;
    string target;
    Query(int idx, string source, string target) {
        this->idx = idx; 
        this->source = source; 
        this->target = target;
    }
};

bool comp_query(Query &q1, Query &q2){
    return q1.idx < q2.idx;
}

struct Clip{
    int start;
    int end;
    string str_clip;
    Clip(int start, int end, string str_clip){
        this->start = start;
        this->end = end;
        this->str_clip = str_clip;
    }
};


class Solution {
public:
    string findReplaceString(string s, vector<int>& indices, vector<string>& sources, vector<string>& targets) {
        return solve(s, indices, sources, targets);
    }

    string solve(string s, vector<int>& indices, vector<string>& sources, vector<string>& targets) {
        /*
        This solution replace the clips from tail to head.
        */
        vector<Query> queries;
        for(int i=0; i<indices.size(); i++){
            Query query(indices[i], sources[i], targets[i]);
            queries.push_back(query);
        }
        sort(queries.begin(), queries.end(), comp_query);
        reverse(queries.begin(), queries.end());

        string res = s;
        for(auto q : queries){
            int idx = q.idx;
            string source = q.source;
            string target = q.target;
            if (s.substr(idx, source.length()) == source){
                int p_id = idx; 
                int s_id = min(idx+source.length(), res.length());
                string prefix = res.substr(0, p_id);
                string suffix = res.substr(s_id);
                res = prefix + target + suffix;
            }
        }
        return res;
    }

    string solve_split(string s, vector<int>& indices, vector<string>& sources, vector<string>& targets) {
        /*
        This solution split the origin s into non-replaced clips and then merge them with the replaced target clips in order;
        */
        vector<Query> queries;
        for(int i=0; i<indices.size(); i++){
            Query query(indices[i], sources[i], targets[i]);
            queries.push_back(query);
        }
        sort(queries.begin(), queries.end(), comp_query);

        // vector<
        // vector<int>
        vector<int> idxs = {0,};
        vector<Query> valid_queries;
        for(auto q : queries){
            int idx = q.idx;
            string source = q.source;
            string target = q.target;
            // cout << idx << " " << source << " " << target << "\n";
            if (s.substr(idx, source.length()) == source){
                // cout << "here" << "\n";
                idxs.push_back(idx);
                idxs.push_back(idx + source.length());
                valid_queries.push_back(q);
            }
        }
        idxs.push_back(s.length());
        // print_vec(idxs);

        string res;
        for(int i=0; i<idxs.size()-1; i++){
            if (i % 2 == 0){ // origin string
                int start = idxs[i], end = idxs[i+1];
                res += s.substr(start, end-start);
            }
            else{
                res += valid_queries[i/2].target;
            }
        }

        return res;
    }
};

int main(){
    string s;
    vector<int> idxs;
    vector<string> sources, targets;
    s = "abcd"; idxs = {0, 2}; sources = {"a", "cd"}; targets = {"eee", "ffff"};
    // s = "ggabcd"; idxs = {2, 5}; sources = {"ab","ec"}; targets = {"eee","ffff"};
    // s = "vmokgggqzp"; idxs = {3,5,1}; sources = {"kg","ggq","mo"}; targets = {"s","so","bfr"};
    // s = "mhnbzxkwzxtaanmhtoirxheyanoplbvjrovzudznmetkkxrdmr"; idxs = {46,29,2,44,31,26,42,9,38,23,36,12,16,7,33,18}; sources = {"rym","kv","nbzxu","vx","js","tp","tc","jta","zqm","ya","uz","avm","tz","wn","yv","ird"}; targets = {"gfhc","uq","dntkw","wql","s","dmp","jqi","fp","hs","aqz","ix","jag","n","l","y","zww"};

    Solution sol;
    string res = sol.findReplaceString(s, idxs, sources, targets);
    cout << res << "\n";
    return 0;
}