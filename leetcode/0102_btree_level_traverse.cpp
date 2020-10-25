/* Binary Tree Level Order Traversal
 * https://leetcode.com/problems/binary-tree-level-order-traversal/
 */

#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
#include <stack>
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


TreeNode *build_tree(){
    TreeNode *root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);
    return root;
}


class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        return solve(root);
    }

    vector<vector<int>> solve(TreeNode *root){
        queue<int> depth_q;
        queue<TreeNode*> t_q;
        vector<vector<int>> res;
        t_q.push(root);
        depth_q.push(1);
        while(! t_q.empty()){
            TreeNode *node = t_q.front();
            t_q.pop();
            int depth = depth_q.front();
            depth_q.pop();
            if (node != nullptr){
                if (res.size() < depth){
                    vector<int> mid_res;
                    mid_res.push_back(node->val);
                    res.push_back(mid_res);
                }
                else{
                    res[depth-1].push_back(node->val);
                }
                t_q.push(node->left);
                t_q.push(node->right);
                depth_q.push(depth+1);
                depth_q.push(depth+1);
            }
        }
        return res;
    }
};


int main(){
    TreeNode *p = build_tree();
    Solution sol;
    vector<vector<int>> res = sol.levelOrder(p);
    cout << res.size() << "\n";
    for(int i=0; i<res.size(); i++){
        for(int j=0; j<res[i].size(); j++){
            cout << res[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
