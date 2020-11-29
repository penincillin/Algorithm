/* Convert Sorted List to Binary Search Tree
 * https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
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

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
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

ListNode * vec2list(vector<int> nums){
    if (nums.size() == 0){
        return nullptr;
    }
    else{
        ListNode *head = new ListNode(nums[0]);
        ListNode *prev = head;
        for(int i=1; i<nums.size(); i++){
            ListNode *cur = new ListNode(nums[i]);
            prev->next = cur;
            prev = cur;
        }
        return head;
    }

}

void print_list(ListNode *head){
    while(head != nullptr){
        cout << head->val << " ";
        head = head->next;
    }
    cout << "\n";
}


class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if (head == nullptr){
            return nullptr;
        }
        else{
            vector<int> nums;
            while(head != nullptr){
                nums.push_back(head->val);
                head = head->next;
            }
            return solve(nums, 0, nums.size());
        }
    }

    TreeNode* solve(vector<int> &nums, int head, int tail){
        if (head >= tail){
            return nullptr;
        }
        else{
            int mid = (head+tail)/2;
            TreeNode *root = new TreeNode(nums[mid]);
            TreeNode *left = solve(nums, head, mid);
            TreeNode *right = solve(nums, mid+1, tail);
            root->left = left;
            root->right = right;
            return root;
        }
    }
};


int main(){
    vector<int> nums{-10, -3, 0, 5, 9};
    ListNode *head = vec2list(nums);
    //print_list(head);
    Solution sol;
    TreeNode *root = sol.sortedListToBST(head);
    print_tree(root, "inorder");
    print_tree(root, "preorder");
    return 0;
}
