/* Symmetric Tree https://leetcode.com/problems/symmetric-tree/
 */

#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
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

/*
TreeNode * buildTree(){
    TreeNode *root = new TreeNode(1);
    TreeNode *left = new TreeNode(2);
    TreeNode *right = new TreeNode(2);
    root->left = left;
    root->right = right;
    left->left = new TreeNode(3);
    left->right = new TreeNode(4);
    right->left = new TreeNode(4);
    right->right = new TreeNode(3);
    return root;
}
*/

TreeNode *buildTree(){
    TreeNode *root = new TreeNode(1);
    TreeNode *left = new TreeNode(2);
    TreeNode *right = new TreeNode(2);
    root->left = left;
    root->right = right;
    left->right = new TreeNode(3);
    right->right = new TreeNode(3);
    return root;
}

class Solution {
public:

    bool isSymmetric(TreeNode* root) {
        if (root == nullptr){
            return true;
        }
        else{
            //return solve(root->left, root->right);
            return solve_iter(root);
        }
    }

    bool solve_iter(TreeNode *root){
        queue<TreeNode *> q1;
        queue<TreeNode *> q2;
        q1.push(root->left);
        q2.push(root->right);
        cout << root << "\n";
        //cout << root->left << " " << root->right << "\n";
        while(! q1.empty()){
            TreeNode *left = q1.front();
            TreeNode *right = q2.front();
            //cout << left->val << " " << right->val << " " << "\n";
            q1.pop();
            q2.pop();
            if (left == nullptr && right == nullptr){
                continue;
            }
            else if (left == nullptr || right == nullptr){
                return false;
            }
            else{
                if (left->val == right->val){
                    q1.push(left->left); q2.push(right->right);
                    q1.push(left->right); q2.push(right->left);
                }
                else{
                    return false;
                }
            }
        }
        return true;
    }
    
    bool solve(TreeNode *left, TreeNode *right){
        if (left == nullptr && right == nullptr){
            return true;
        }
        else if (left == nullptr || right == nullptr){
            return false;
        }
        else{
            if (left->val == right->val){
                return solve(left->left, right->right) && solve(left->right, right->left);
            }
            else{
                return false;
            }
        }
    }
};


int main(){
    TreeNode *root = buildTree();
    //print_tree(root, "inorder");
    //print_tree(root, "preorder");
    Solution sol;
    bool res = sol.isSymmetric(root);
    cout << res << "\n";
    return 0;
}
