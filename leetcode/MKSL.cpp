#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode* buildList(int *array, int N){
    ListNode *start = new ListNode(-1);
    ListNode *head = start;
    for(int i=0; i<N; i++){
        ListNode *node = new ListNode(array[i]);
        head->next = node;
        head = node;
    }
    return start->next;
}
void printNode(ListNode *head){
    while(head != NULL){
        cout << head->val << " ";
        head = head->next;
    }
    cout << "\n";
}
void deleteNode(ListNode *head){
    while(head != NULL){
        ListNode *tmp = head;
        delete tmp;
        head = head->next;
    }
}

struct IDListNode{
    ListNode *node;
    int list_id;
    IDListNode(ListNode *node_param, int id_param){
        node = node_param;
        list_id = id_param;
    }
};

class MyCmp{
    public:
    bool operator()(const IDListNode &l1, const IDListNode l2){
        return l1.node->val > l2.node->val;
    }
};

typedef priority_queue<IDListNode, vector<IDListNode>, MyCmp> myqueue;

class Solution {
public:
    myqueue buildQueue(vector<ListNode*>& lists){
        myqueue queue;
        for(unsigned i=0; i<lists.size(); i++){
            if(lists[i]!=NULL){
                IDListNode inode(lists[i],i);
                lists[i] = lists[i]->next;
                queue.push(inode);
            }
        }
        return queue;
    }
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode *start = new ListNode(-1);
        ListNode *head = start;
        myqueue queue = buildQueue(lists);
        while(!queue.empty()){
            IDListNode inode = queue.top();
            queue.pop();
            head->next = inode.node;
            head = head->next;
            int pop_id = inode.list_id;
            if(lists[pop_id]!=NULL){
                IDListNode jnode(lists[pop_id], pop_id);
                lists[pop_id] = lists[pop_id]->next;
                queue.push(jnode);
            }
        }
        return start->next;
    }
};

int main(){
    int A1[] = {1, 4, 7, 10, 12};
    ListNode *head1 = buildList(A1, 5);
    int A2[] = {2, 3, 5, 14};
    ListNode *head2 = buildList(A2, 4);
    int A3[] = {6, 11, 13, 16, 18};
    ListNode *head3 = buildList(A3, 5);
    vector<ListNode*> lists;
    lists.push_back(head1);
    lists.push_back(head2);
    lists.push_back(head3);
    Solution ss;
    ListNode *res = ss.mergeKLists(lists);
    printNode(res);
    return 0;
}
