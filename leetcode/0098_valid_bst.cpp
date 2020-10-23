/* Validate Binary Search Tree, https://leetcode.com/problems/validate-binary-search-tree/
 * In this version, I implement recursion, but this code can be implemented with in-order traverse
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

TreeNode* build_tree(){
    /*
    TreeNode *root = new TreeNode(2);
    root->left = new TreeNode(1);
    root->right = new TreeNode(3);
    */
    TreeNode *root = new TreeNode(5);
    TreeNode *left = new TreeNode(1);
    TreeNode *right = new TreeNode(4);
    root->left = left;
    root->right = right;
    right->left = new TreeNode(3);
    right->right = new TreeNode(6);
    return root;
}

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return solve(root, -2147483649, 2147483648);
    }
    bool solve(TreeNode *root, long long low, long long high){
        if (root == nullptr){
            return true;
        }
        else{
            long long val = root->val;
            if (val > low && val < high){
                bool left_valid = solve(root->left, low, min(high, val));
                bool right_valid = solve(root->right, max(low,val), high);
                return left_valid && right_valid;
            }
            else{
                return false;
            }
        }
    }
};


int main(){
    TreeNode *root = build_tree();
    print_tree(root, "inorder");
    Solution sol;
    bool res = sol.isValidBST(root);
    cout << res << "\n";
    return 0;
}
