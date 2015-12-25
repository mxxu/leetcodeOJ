#include <stdio.h>
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


struct ListNode *findMidNode(struct ListNode *head) {
  if (!head) return head;
  struct ListNode *slow = head, *fast = head;

  while (fast->next && fast->next->next) {
    slow = slow->next;
    fast = fast->next->next;
  }
  return slow;
}

struct ListNode *reverse(struct ListNode *head) {
  if (!head || !head->next) return head;

  struct ListNode *prev = head, *curr = head->next;
  struct ListNode *next = curr->next;

  prev->next = 0;
  while (curr) {
    curr->next = prev;
    prev = curr;
    curr = next;

    if (!curr)
      break;
    next = curr->next;
  }
  return prev;
}

void reorderList(struct ListNode *head) {
  // reverse right half list, then merge two list

  if (!head || !head->next || !head->next->next) return;

  // find mid node
  struct ListNode *mid = findMidNode(head);

  // reverse right half
  struct ListNode *rev = reverse(mid->next);

  // split to two lists
  mid->next = 0;

  // merge
  struct ListNode *left = head;
  while (rev) {
    struct ListNode *ltmp = left->next;
    struct ListNode *rtmp = rev->next;
    left->next = rev;
    rev->next = ltmp;

    left = ltmp;
    rev = rtmp;
  }
}

void printList(struct ListNode *head) {
  while (head) {
    printf("%d, ", head->val);
    head = head->next;
  }
}

int main(int argc, char const *argv[])
{
  struct ListNode a, b, c, d, e;
  a.next = &b;
  b.next = &c;
  c.next = &d;
  d.next = 0;
  e.next = 0;

  a.val = 1;
  b.val = 2;
  c.val = 3;
  d.val = 4;
  e.val = 5;

  //printList(&a);

  struct ListNode *mid = findMidNode(&a);
  printf("%d\n", mid->val);

  reorderList(&a);
  printList(&a);

  struct ListNode *rev = reverse(&a);
  printList(rev);
  return 0;
}
