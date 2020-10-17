/* Binary Tree Inorder Traversal, https://leetcode.com/problems/binary-tree-inorder-traversal/
 * No-recursion version: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
 */

#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
using namespace std;

template <typename T>
void print_vec(vector<T> vec){
    for(int i=0; i<vec.size(); i++){
        cout << vec[i] << " ";
    }
    cout << "\n";
}

template <typename T>
void print_vec_II(vector<vector<T>> vec){
    for(int i=0; i<vec.size(); i++){
        for(int j=0; j<vec[i].size(); j++){
            cout << vec[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "------------------\n";
}


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


TreeNode * build_tree(){
    TreeNode *root = new TreeNode(1);
    TreeNode *n1 = new TreeNode(2);
    TreeNode *n2 = new TreeNode(3);
    root->right = n1;
    n1->left = n2;
    return root;
}


int main(){
    TreeNode *root = build_tree();
    return 0;
}
