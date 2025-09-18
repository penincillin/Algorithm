/* Same Tree
 * https://leetcode.com/problems/same-tree/
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
    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    return root;
}


class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return solve_iter(p, q); 
    }

    bool solve_iter(TreeNode *p, TreeNode *q){
        queue<TreeNode*> stack_p;
        queue<TreeNode*> stack_q;
        stack_p.push(p);
        stack_q.push(q);
        while(! stack_p.empty()){
            p = stack_p.front();
            q = stack_q.front();
            stack_p.pop();
            stack_q.pop();
            if (p == nullptr && q == nullptr){
                // pass
            }
            else if (p != nullptr && q != nullptr){
                if (p->val == q->val){
                    stack_p.push(p->left);
                    stack_p.push(p->right);
                    stack_q.push(q->left);
                    stack_q.push(q->right);
                }
                else{
                    return false;
                }
            }
            else{
                return false;
            }
        }
        return true;
    }

    bool solve(TreeNode *p, TreeNode *q){
        if (p == nullptr && q == nullptr){
            return true;
        }
        else if (p != nullptr && q != nullptr){
            if (p->val == q->val){
                bool left = solve(p->left, q->left);
                bool right = solve(p->right, q->right);
                return left && right;
            }
            else{
                return false;
            }
        }
        else{
            return false;
        }
    }
};


int main(){
    TreeNode *p = build_tree();
    TreeNode *q = build_tree();
    Solution sol;
    bool res = sol.isSameTree(p, q);
    cout << res << "\n";
    return 0;
}
