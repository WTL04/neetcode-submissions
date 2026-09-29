/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
        ListNode* curr_a = headA;
        ListNode* curr_b = headB;
        int length_a = 0;
        int length_b = 0;

        // first pass: get length of both lists
        while (curr_a != nullptr) {
            length_a++;
            curr_a = curr_a->next;
        }
        while (curr_b != nullptr) {
            length_b++;
            curr_b = curr_b->next;
        }

        // find shortest list
        int diff;
        ListNode* shorter_list;
        ListNode* longer_list;

        if (length_a < length_b) {
            diff = length_b - length_a;
            shorter_list = headA;
            longer_list = headB;
        }
        else {
            diff = length_a - length_b;
            shorter_list = headB;
            longer_list = headA; 
        }

        // make longer list start at the same index as shorter list
        for (int i = 0; i < diff; i++) {
            longer_list = longer_list->next;
        }

        // second pass: compare if nodes are equal
        while (shorter_list != nullptr && longer_list != nullptr) {
            if (shorter_list == longer_list) {
                return shorter_list;
            } 
            shorter_list = shorter_list->next;
            longer_list = longer_list->next;
        }
        return 0;
    }
};