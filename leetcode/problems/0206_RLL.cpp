/* easy
 * this algorithm could be implemented in iteration or recursive version
 * recurvise version is easy to understand
 * for iteration version, suppose the original list is [1]->[2]->[3]->[4]->[5]->[6]->[7]...
 * we reverse the first two nodes, make it [1]<-[2]->[3]->[4]...
 * then the second and third nodes, make it [1]<-[2]<-[3]->[4].. 
 * repeat this process until we get all node reversed
 * complexity of this algorithm is O(n)
 */


#include <iostream>
#include <vector>

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
    ListNode* recursive(ListNode* head) {
        if (head==NULL || head->next==NULL){
            return head;
        }
        else{
            ListNode *new_head = recursive(head->next);
            head->next->next = head;
            head->next = NULL;
            return new_head;
        }
    }

    ListNode* iteration(ListNode *head){
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

    ListNode *reverseList(ListNode *head){
        return iteration(head);
    }
};


int main(){
    int A1[] = {1, 2, 3, 4};
    ListNode *head1 = buildList(A1, 1);
    Solution ss;
    ListNode *res = ss.reverseList(head1);
    printNode(res);
    return 0;
}
