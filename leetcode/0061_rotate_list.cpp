/* Rotate List, https://leetcode.com/problems/rotate-list/
 * Not hard, pay attention to that: 1.list can be empty. 2.k > len(list)
 */
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
using namespace std;

struct ListNode{
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void print_list(ListNode *head){
    while(head != NULL){
        cout << head->val << " "; 
        head = head->next;
    }
    cout << "\n";
}
 
class Solution {
private:
    int get_len(ListNode* head){
        int len = 0;
        while(head != NULL){
            len ++;
            head = head->next;
        }
        return len;
    }
public:
    ListNode* rotateRight(ListNode* head, int k) {
        int len = get_len(head);
        if (len == 0){
            return head;
        }
        k = k % len;
        if (k == 0){
            return head;
        }
        
        ListNode *new_tail, *new_head, *old_tail;
        ListNode *cur = head;
        for(int i=0; i<len; i++){
            if (i == len-k-1){
                new_tail = cur;
                new_head = cur->next;
            }
            if (i == len-1){
                old_tail = cur;
            }
            cur = cur->next;
        }
        old_tail->next = head;
        new_tail->next = NULL;
        return new_head;
    }
};

int main(){
    int vals[5] = {1,2,3,4,5};
    ListNode *head = new ListNode(vals[0]);
    /*
    ListNode *cur = head;
    for(int i=1; i<5; i++){
        ListNode *next = new ListNode(vals[i]);
        cur->next = next;
        cur = next;
    }
    */
    int k = 6;
    //print_list(head);

    Solution sol;
    ListNode *res = sol.rotateRight(head, k);
    print_list(res);
    return 0;
}
