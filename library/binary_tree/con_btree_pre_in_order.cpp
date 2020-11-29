/* Construct Binary Tree from Preorder and Inorder Traversal, 
 * https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
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
        print_preorder(root);
        cout << "\n";
    }
}

class Solution {
private:
    unordered_map<int, int> my_map;
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.size() == 0){
            return nullptr;
        }
        else{
            int n = preorder.size();
            for(int i=0; i<n; i++){
                my_map[inorder[i]] = i;
            }
            TreeNode *root = solve(preorder, inorder, 0, n, 0, n);
            return root;
        }
    }

    TreeNode *solve(vector<int>& preorder, vector<int>& inorder, int pre_head, int pre_tail, int in_head, int in_tail){
        if (pre_head < pre_tail){
        //if (pre_head < pre_tail){
            int val = preorder[pre_head];
            TreeNode *root = new TreeNode(val);

            int new_head = my_map[val];

            int new_pre_head = pre_head + 1;
            int new_pre_tail = new_pre_head + (new_head-in_head);
            int new_in_head = in_head;
            int new_in_tail = new_head;

            int new_in_head0 = new_head + 1;
            int new_in_tail0 = in_tail;
            int new_pre_head0 = new_pre_tail;
            int new_pre_tail0 = pre_tail;

            TreeNode *left = solve(preorder, inorder, new_pre_head, new_pre_tail, new_in_head, new_in_tail);
            TreeNode *right = solve(preorder, inorder, new_pre_head0, new_pre_tail0, new_in_head0, new_in_tail0);

            root->left = left;
            root->right = right;
            return root;
        }
        else{
            return nullptr;
        }
    }
};

int main(){
    Solution sol;
    vector<int> pre{3,9,20,15,7};
    vector<int> in{9,3,15,20,7};
    //vector<int> pre{1, 2, 3};
    //vector<int> in{3, 2, 1};
    TreeNode *root = sol.buildTree(pre, in);
    print_tree(root, "preorder");
    print_tree(root, "inorder");
    return 0;
}
