/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode {
  int val;
  struct ListNode *next;
};

struct ListNode *swapPairs(struct ListNode *head) {
  if (!head || !head->next) return head;

  struct ListNode *new_head = head->next;
  struct ListNode *p = new_head->next;

  new_head->next = head;
  head->next = swapPairs(p);

  return new_head;
}
