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

class Solution {
private:
    unordered_map<int, int> my_map;
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (inorder.size() == 0){
            return nullptr;
        }
        else{
            int n = inorder.size();
            for(int i=0; i<n; i++){
                my_map[inorder[i]] = i;
            }
            TreeNode *root = solve(inorder, postorder, 0, n, 0, n);
            return root;
        }
    }

    TreeNode *solve(vector<int>& inorder, vector<int>& postorder, int in_head, int in_tail, int post_head, int post_tail){
        if (in_head < in_tail && post_head < post_tail){
            int val = postorder[post_tail-1];
            int new_head = my_map[val];

            int new_in_head = in_head;
            int new_in_tail = new_head;
            int new_post_head = post_head;
            int new_post_tail = new_post_head + (new_in_tail - new_in_head);

            int new_in_head0 = new_head + 1;
            int new_in_tail0 = in_tail;
            int new_post_head0 = new_post_tail;
            int new_post_tail0 = post_tail-1;

            /*
            cout << new_in_head << " " << new_in_tail << " " << new_post_head << " " << new_post_tail << "\n";
            cout << new_in_head0 << " " << new_in_tail0 << " " << new_post_head0 << " " << new_post_tail0 << "\n";
            cout << "------------------\n";
            */

            TreeNode *root = new TreeNode(val);
            root->left = solve(inorder, postorder, new_in_head, new_in_tail, new_post_head, new_post_tail);
            root->right = solve(inorder, postorder, new_in_head0, new_in_tail0, new_post_head0, new_post_tail0);
            //cout << "val: " << root->val << " point: " << root->left << " " << root->right << "\n";
            return root;
        }
        else{
            return nullptr;
        }
    }
};

int main(){
    vector<int> in{9,3,15,20,7};
    vector<int> post{9,15,7,20,3};
    
    //vector<int> in{3, 9};
    //vector<int> post{3, 9};

    Solution sol;
    TreeNode *root = sol.buildTree(in, post);
    print_tree(root, "inorder");
    print_tree(root, "postorder");
    return 0;
}
