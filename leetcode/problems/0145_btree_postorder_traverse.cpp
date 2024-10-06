/* Binary Tree postorder Traversal, https://leetcode.com/problems/binary-tree-postorder-traversal/
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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        solve(root, res);
        return res;
    }

    void solve_iterate(TreeNode *root, vector<int>& res){
        if (root == nullptr){
            return;
        }
        else{
            bool visit[101];
            memset(visit, 0, 101);
            TreeNode *stack[101];
            stack[0] = root;
            int tail=0;
            TreeNode* curr;
            while(tail >= 0){
                curr = stack[tail];
                if (curr->left != nullptr){
                    stack[++tail] = curr->left;
                    visit[tail] = false;
                    curr = curr->left;
                }
                if (! visit[tail]){
                    if (curr->right != nullptr){
                        visit[tail] = true;
                        stack[++tail] = curr->right;
                        curr = curr->right;
                    }
                    else{
                        res.push_back(curr->val);
                        tail--;
                    }
                }
                else{
                    res.push_back(curr->val);
                    tail--;
                }
            }
        }
    }

    void solve(TreeNode* root, vector<int>& res){
        if (root != nullptr){
            solve(root->left, res);
            solve(root->right, res);
            res.push_back(root->val);
        }
    }
};


int main(){
    TreeNode *root = build_tree();
    Solution sol;
    vector<int> res = sol.postorderTraversal(root);
    print_vec(res);
    return 0;
}
