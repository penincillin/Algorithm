/*
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
    Node* child[26];
    bool is_word;
    set<int> word_ids;
    Node(){
        is_word = false;
        for(int i=0; i<26; i++){
            child[i] = NULL;
        }
    }
};

class Trie {
private:
    Node root;
public:
    Trie() { }
    void insert(string word, int word_id) {
        Node* node = &root;
        for(char c : word){
            int child_idx = c - 'a';
            if (node->child[child_idx]){
                node  = node->child[child_idx];
            }
            else{
                Node *new_node = new Node(); // must use new here.
                node->child[child_idx] = new_node;
                node = new_node;
            }
            node->word_ids.insert(word_id);
        }
        node->is_word = true;
    }
    set<int> startsWith(string prefix) {
        Node *node = &root;
        for(auto c : prefix){
            int child_idx = c - 'a';
            if (node->child[child_idx]){
                node = node->child[child_idx];
            }
            else{
                return set<int> ();
            }
        }
        return node->word_ids;
    }
}; 

template <typename T>
void print_set(set<T> s){
    for(auto s0 : s){
        cout << s0 << " ";
    }
    cout << "\n";
}

class WordFilter {
private:
    Trie trie_prefix;
    Trie trie_suffix;
    string reverse_word(string word){
        reverse(word.begin(), word.end());
        return word;
    }
public:
    WordFilter(vector<string>& words) {
        int word_id = 0;
        for(auto word : words){
            trie_prefix.insert(word, word_id);
            trie_suffix.insert(reverse_word(word), word_id);
            word_id += 1;
        }
    }
    
    int f(string prefix, string suffix) {
        set<int> s0 = trie_prefix.startsWith(prefix);
        set<int> s1 = trie_suffix.startsWith(reverse_word(suffix));
        // print_set(s0);
        // print_set(s1);
        vector<int> inter_vec;
        set_intersection(s0.begin(), s0.end(), s1.begin(), s1.end(), 
            inserter(inter_vec, inter_vec.begin()));
        if (inter_vec.size() > 0){
            return *(inter_vec.end()-1);
        }
        else{
            return -1;
        }
    }
};

int main(){
    vector<string> words;
    string prefix, suffix;
    // words = {"apple", "appllle", "bellle"}; prefix = "a"; suffix = "e";
    words = {"cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"};
    // prefix = "bccbacbcba"; suffix = "a";
    // prefix = "ab"; suffix = "abcaccbcaa";
    prefix = "a"; suffix = "aa";


    WordFilter wf(words);
    int res = wf.f(prefix, suffix);
    cout << res << "\n";
    return 0;
}