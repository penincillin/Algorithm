/*173. Binary Search Tree Iterator. https://leetcode.com/problems/binary-search-tree-iterator/
 * Idea: Inorder traversal the whole binary-tree
 */

class BSTIterator {
private:
    vector<int> node_list;
    int idx;
    void build_list(TreeNode *node){
        if (node==NULL){
            return;
        }
        if (node->left != NULL){
            build_list(node->left);
        }
        node_list.push_back(node->val);
        if (node->right != NULL){
            build_list(node->right);
        }
    }

public:
    BSTIterator(TreeNode* root) {
        build_list(root);
        idx = 0;
    }
    
    /** @return the next smallest number */
    int next() {
        idx += 1;
        return node_list[idx-1];
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return idx<node_list.size();
    }
};
