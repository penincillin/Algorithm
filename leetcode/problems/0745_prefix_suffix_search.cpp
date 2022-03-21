/*
Prefix and Suffix Search, https://leetcode.com/problems/prefix-and-suffix-search/
Suppose the number of words, the length of word and the number of querry are N, K, and Q, respectively,
The code written in prefix_suffix_search_backup.cpp is O(N*K + Q(N+K)). N*K for building trie, N in Q(N+K) is the time complexity of merge set.
The code in this file is O(N*K^2 + QK)
Since the K is relatively smaller than N and Q (10 V.S. 10000), the latter one is faster
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

class Node{
public:
    Node* child[27]; // 'a'~'z' + '#'
    bool is_word;
    int word_id = -1;
    Node(){
        is_word = false;
        for(int i=0; i<27; i++){
            child[i] = NULL;
        }
    }
};

class Trie {
private:
    Node root;
    int char2idx(char c){
        int child_idx = c - 'a';
        child_idx = (child_idx<0 || child_idx>25) ? 26 : child_idx;
        // cout << c << " " << child_idx << "\n";
        return child_idx;
    }
public:
    Trie() { }
    void insert(string word, int word_id) {
        Node* node = &root;
        for(char c : word){
            // int child_idx = c - 'a';
            int child_idx = char2idx(c);
            if (node->child[child_idx]){
                node  = node->child[child_idx];
            }
            else{
                Node *new_node = new Node(); // must use new here.
                node->child[child_idx] = new_node;
                node = new_node;
            }
            node->word_id = max(node->word_id, word_id);
        }
        node->is_word = true;
    }
    int startsWith(string prefix) {
        Node *node = &root;
        for(auto c : prefix){
            // int child_idx = c - 'a';
            int child_idx = char2idx(c);
            if (node->child[child_idx]){
                node = node->child[child_idx];
            }
            else{
                return -1;
            }
        }
        return node->word_id;
    }
}; 

class WordFilter {
private:
    Trie trie;
public:
    WordFilter(vector<string>& words) {
        int word_id = 0;
        for(auto word : words){
            for (int i=0; i<word.length(); i++){
                // for (int j=0; j<word.length(); j++){ // 
                    // string prefix = word.substr(0, i);
                    string suffix = word.substr(i);
                    string key = suffix + "#" + word;
                    // cout << "key: " << key << "\n";
                    trie.insert(key, word_id);
            }
            word_id += 1;
        }
    }
    
    int f(string prefix, string suffix) {
        string word = suffix + "#" + prefix;
        int res = trie.startsWith(word);
        return res;
    }
};

int main(){
    vector<string> words;
    string prefix, suffix;
    words = {"apple"}; prefix = "a"; suffix = "e";
    // words = {"apple", "appllle", "bellle"}; prefix = "a"; suffix = "e";
    // words = {"cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"};
    // prefix = "bccbacbcba"; suffix = "a";
    // prefix = "ab"; suffix = "abcaccbcaa";
    // prefix = "a"; suffix = "aa";


    WordFilter wf(words);
    int res = wf.f(prefix, suffix);
    cout << res << "\n";
    return 0;
}