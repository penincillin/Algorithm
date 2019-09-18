#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution{
    public:
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2){
            ListNode head(0);           
            ListNode *preNode = &head;
            int add = 0;
            ListNode *b1 = l1, *b2 = l2;
            while(b1!=NULL || b2!=NULL || add>0){
                ListNode *node = new ListNode(0);
                int val1 = b1 ? b1->val : 0;
                int val2 = b2 ? b2->val : 0;
                b1 = b1 ? b1->next : NULL;
                b2 = b2 ? b2->next: NULL;
                node->val = (val1 + val2 + add) % 10;
                add = (val1 + val2 + add) / 10;
                preNode->next = node;
                preNode = node;
            }
            return head.next;
        }
};

ListNode *getList(int *A, int N){
    ListNode head(0);
    ListNode *preNode = &head;
    for(int i=0; i<N; i++){
        ListNode *node = new ListNode(A[i]);
        preNode->next = node;
        preNode = node;
        //cout << &head << " " << node << endl;
    }
    return head.next;
}

int main(){
    int A[3] = {1, 2, 4};
    int B[3] = {9, 7, 5};
    ListNode *l1 = getList(A, 3);
    ListNode *l2 = getList(B, 3);

    Solution solve;
    ListNode * res = solve.addTwoNumbers(l1, l2);
    while(res){
        cout << res->val <<  " ";
        res = res->next;
    }
    cout << endl;

    return 0;
}
