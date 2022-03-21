/* 
 * Delete Nodes And Return Forest, https://leetcode.com/problems/delete-nodes-and-return-forest/
 */

#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <set>
#include <unordered_set>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

void print_preorder(TreeNode* root){
    if (root != nullptr){
        cout << root->val << " ";
        print_preorder(root->left);
        print_preorder(root->right);
    }
}

void print_inorder(TreeNode* root){
    if (root != nullptr){
        print_inorder(root->left);
        cout << root->val << " ";
        print_inorder(root->right);
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
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(7);
    return root;
}

class Solution {
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_set<int> vals_del;
        for(auto val : to_delete){
            vals_del.insert(val);
        }
        return solve_iter(root, vals_del);
    }

    vector<TreeNode*> solve_iter(TreeNode *root, unordered_set<int>& vals_del){
        typedef pair<TreeNode*, bool> node_info; // bool means has_parent;
        queue<node_info> queue;
        queue.push(make_pair(root, false));

        vector<TreeNode*> res;
        while(queue.size() > 0){
            node_info ni = queue.front(); queue.pop();
            TreeNode* node = ni.first; 
            bool has_parent = ni.second;
            bool to_delete = vals_del.find(node->val) != vals_del.end();

            if (! to_delete && ! has_parent){
                res.push_back(node);
            }

            has_parent = ! to_delete; // this has_parent is for child
            if (node->left != NULL){
                queue.push(make_pair(node->left, has_parent));
                if (vals_del.find(node->left->val) != vals_del.end()){
                    node->left = NULL;
                }
            }

            if (node->right != NULL){
                queue.push(make_pair(node->right, has_parent));
                if (vals_del.find(node->right->val) != vals_del.end()){
                    node->right = NULL;
                }
            }
        }
        return res;
    }

    vector<TreeNode*> solve_recur(TreeNode *root, unordered_set<int>& vals_del){
        if (root == NULL){
            return {};
        }
        else{
            int val = root->val;
            vector<TreeNode*> left_res = solve_recur(root->left, vals_del);
            vector<TreeNode*> right_res = solve_recur(root->right, vals_del);

            if (vals_del.find(val) != vals_del.end()){
                left_res.insert(left_res.end(), right_res.begin(), right_res.end());
                return left_res;
            }

            else{
                vector<TreeNode*> res;
                res.push_back(root);

                if (root->left != NULL){
                    int left_val = root->left->val;
                    if (vals_del.find(left_val) != vals_del.end()){
                        // left node to be delete
                        root->left = NULL;
                        res.insert(res.end(), left_res.begin(), left_res.end());
                    }
                    else{
                        res.insert(res.end(), left_res.begin()+1, left_res.end());
                    }
                }

                if (root->right != NULL){
                    int right_val = root->right->val;
                    if (vals_del.find(right_val) != vals_del.end()){
                        // right node to be delete
                        root->right = NULL;
                        res.insert(res.end(), right_res.begin(), right_res.end());
                    }
                    else{
                        res.insert(res.end(), right_res.begin()+1, right_res.end());
                    }
                }

                return res;
            }
        }
    }
};

int main(){
    TreeNode *root = build_tree();
    vector<int> to_delete;
    to_delete = {2,3};

    Solution sol;
    vector<TreeNode*> res = sol.delNodes(root, to_delete);
    cout << "num of tree: " << res.size() << "\n";
    for(auto tree_node : res){
        print_tree(tree_node, "preorder");
    }
    return 0;
}
