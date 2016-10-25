#include <iostream>
#include <vector>
#include <queue>
#include <assert.h>

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

class Solution {
public:
    ListNode* reverseList(ListNode *head){
        if (head==NULL || head->next==NULL){
            return head;
        }
        else{
            ListNode *prev = head;
            ListNode *cur = head->next;
            prev->next = NULL;
            while(cur!=NULL){
                ListNode *next = cur->next;
                cur->next = prev;
                prev = cur;
                cur = next;
            }
            return prev;
        }
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head==NULL || head->next==NULL){
            return head;
        }
        else{
            int node_num = 1;
            ListNode *node = head;
            while(node!=NULL && node_num<k){
                node_num += 1;
                node = node->next;
            }
            if(node_num == k && node!=NULL){
                ListNode *new_tail = head;
                ListNode *mid_head = node->next;
                node->next = NULL;
                ListNode *new_head = reverseList(head);
                ListNode *sub_head = reverseKGroup(mid_head, k);
                new_tail->next = sub_head;
                return new_head;
            }
            else{
                return head;
            }
        }
    }
};

int main(){
    int A1[] = {1, 2, 3, 4, 5, 6, 7, 8};
    ListNode *head1 = buildList(A1, 8);
    Solution ss;
    ListNode *res = ss.reverseKGroup(head1, 3);
    printNode(res);
   
    return 0;
}
