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
using namespace std;

template <typename T>
void print_vec(vector<T> vec){
    for(auto v:vec){
        cout << v << " ";
    }
    cout << "\n";
}

class Node{
public:
    Node* child[26];
    bool is_word;
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

    bool _search(string word, bool search_word) {
        Node *node = &root;
        for(auto c : word){
            int child_idx = c - 'a';
            if (node->child[child_idx]){
                node = node->child[child_idx];
            }
            else{
                return false;
            }
        }
        return (search_word && node->is_word) || (!search_word);
    }
   
public:
    Trie() {
    }
    
    void insert(string word) {
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
        }
        node->is_word = true;
    }
    
    bool search(string word) {
        return _search(word=word, true);
    }
    
    bool startsWith(string prefix) {
        return _search(prefix, false);
    }
}; 

int main(){
    Trie trie;
    trie.insert("apple");
    cout << trie.search("apple") << "\n";   // return True
    cout << trie.search("app") << "\n";     // return False
    cout << trie.startsWith("app") << "\n"; // return True
    trie.insert("app");
    cout << trie.search("app") << "\n";     // return True
    return 0;
}