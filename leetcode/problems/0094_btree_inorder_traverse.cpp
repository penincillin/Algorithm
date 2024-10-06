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


class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        //solve_recursive(root, res);
        solve_iterate_v2(root, res);
        return res;
    }

    void solve_iterate_v1(TreeNode *root, vector<int>& res){
        if (root == nullptr){
            return;
        }
        else{
            TreeNode * stack[110];
            stack[0] = root;
            int head = 0, tail = 0;
            TreeNode *curr = root;
            bool check_left = true;
            while(head <= tail){
                if (curr->left != nullptr && check_left){
                    stack[tail] = curr;
                    tail ++;
                    curr = curr->left;
                }
                else{
                    res.push_back(curr->val);
                    if (curr->right != nullptr){
                        curr = curr->right;
                        check_left = true;
                    }
                    else{
                        tail--;
                        curr = stack[tail];
                        check_left = false;
                    }
                }
            }
        }
    }

    void solve_iterate_v2(TreeNode *root, vector<int>& res){
        TreeNode * stack[101];
        TreeNode *cur = root;
        int tail=0;
        while(cur != nullptr || tail>0){
            while(cur != nullptr){
                stack[tail] = cur;
                cur = cur->left;
                tail++;
            }
            cur = stack[tail-1]; 
            tail--;
            res.push_back(cur->val);
            cur = cur->right;
        }
    }

    void solve_recursive(TreeNode *root, vector<int>& res){
        if (root != nullptr){
            solve_recursive(root->left, res);
            res.push_back(root->val);
            solve_recursive(root->right, res);
        }
    }
};




int main(){
    TreeNode *root = build_tree();
    Solution sol;
    vector<int> res = sol.inorderTraversal(root);
    print_vec(res);
    return 0;
}
