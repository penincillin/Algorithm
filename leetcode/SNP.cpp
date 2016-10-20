/* easy
 * just consider two nodes one time, we call these two nodes first and second
 * just save the prev node of first node, next node of second node
 * be care that the second node may not exist(which means second==NULL)
 */


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
    ListNode* swapPairs(ListNode* head) {
        ListNode *start = new ListNode(-1);
        start->next = head;
        ListNode *first = head;
        ListNode *prev = start;
        while(first!=NULL){
            ListNode *second = first->next;
            if(second!=NULL){
                ListNode *post = second->next;
                prev->next = second;
                second->next = first;
                first->next = post;
            }
            prev = first;
            first = first->next;
        }
        return start->next;
    }
};

int main(){
    int A1[] = {1, 2, 3, 4};
    ListNode *head1 = buildList(A1, 3);
    Solution ss;
    ListNode *res = ss.swapPairs(head1);
    printNode(res);
    return 0;
}
