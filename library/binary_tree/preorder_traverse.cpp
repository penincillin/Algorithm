/* Binary Tree preorder Traversal, https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/
 * No-recursion version: https://www.geeksforgeeks.org/iterative-preorder-traversal/
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
    TreeNode *n1 = new TreeNode(4);
    TreeNode *n2 = new TreeNode(3);
    TreeNode *n3 = new TreeNode(2);
    root->left = n1;
    root->right = n2;
    n1->left = n3;
    return root;
}


class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        solve_iterate(root, res);
        return res;
    }

    void solve_iterate(TreeNode *root, vector<int>& res){
        if (root == nullptr){
            return;
        }
        else{
            TreeNode *stack[101];
            int head=0, tail=0;
            stack[head] = root;
            TreeNode *cur;
            while(tail >= 0){
                cur = stack[tail];
                tail--;
                if (cur != nullptr){
                    res.push_back(cur->val);
                    stack[++tail] = cur->right;
                    stack[++tail] = cur->left;
                }
            }
        }
    }

    void solve(TreeNode* root, vector<int>& res){
        if (root != nullptr){
            res.push_back(root->val);
            solve(root->left, res);
            solve(root->right, res);
        }
    }
};


int main(){
    TreeNode *root = build_tree();
    Solution sol;
    vector<int> res = sol.preorderTraversal(root);
    print_vec(res);
    return 0;
}
