/* Construct Binary Tree from Inorder and Postorder Traversal
 * https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
 */

#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

void print_inorder(TreeNode* root){
    if (root != nullptr){
        print_inorder(root->left);
        cout << root->val << " ";
        print_inorder(root->right);
    }
}

void print_preorder(TreeNode* root){
    if (root != nullptr){
        cout << root->val << " ";
        print_preorder(root->left);
        print_preorder(root->right);
    }
}

void print_postorder(TreeNode* root){
    if (root != nullptr){
        print_postorder(root->left);
        print_postorder(root->right);
        cout << root->val << " ";
    }
}


void print_tree(TreeNode *root, string print_type){
    if (print_type == "inorder"){
        print_inorder(root);
        cout << "\n";
    }
    else if (print_type == "preorder"){
        print_preorder(root);
        cout << "\n";
    }
    else if (print_type == "postorder"){
        print_postorder(root);
        cout << "\n";
    }
}


int main(){
    return 0;
}
