#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

void printList(ListNode *head) {
	while (head) {
		cout << head->val << "->";
		head = head->next;
	}
	cout << endl;
}

class Solution {
public:
	ListNode *merge(ListNode *a, ListNode *b) {
		//cout << "merging...\n";
		//printList(a);
		//printList(b);
		ListNode *head = NULL, *tail = NULL;
		ListNode *smaller = NULL;
		while (a && b) {
			//cout << a->val << " vs " << b->val << endl;
			if (a->val > b->val) {
				smaller = b;
				b = b->next;
			} else {
				smaller = a;
				a = a->next;
			}
			if (!head) {
				head = smaller;
				tail = head;
			} else {
				tail->next = smaller;
				tail = tail->next;
			}
			//cout << smaller->val << ".....\n";
		}
		ListNode *left = a ? a : b;
		while (left) {
			//cout << left->val << " left\n";
			tail->next = left;
			tail = tail->next;
			left = left->next;
		}
		//printList(head);
		return head;
	}
	
	ListNode *sortList(ListNode *head) {
		if (!head) return head;
		return _sortList(head, NULL);
	}
	
    ListNode *_sortList(ListNode *head, ListNode *tail) {
		//cout << (head ? head->val:-1) << " +++ " << (tail ? tail->val : -10000) << endl;
		if (!head) return head;
		if (head == tail || head->next == tail) {
			head->next = NULL;
			return head;
		}
		
		//cout << "@@@@@@ " << head->next->val << endl;
		ListNode *once = head, *twice = head;
		while (twice->next != tail) {
			//cout << once->val << " once value.";
			once = once->next;
			twice = twice->next;
			if (twice->next == tail) break;
			twice = twice->next;
		}
		//cout << head->val << "," << once->val << "," << twice->val << endl;
		if (once == head) once = head->next;
		ListNode *a = _sortList(head, once);
		ListNode *b = _sortList(once, tail);
		return merge(a, b);
    }
};

int main (int argc, char const *argv[])
{
	ListNode a(1), b(2), c(3), d(4), e(5);
	// 1 5 3 4 2
	Solution sol;
	a.next = &b;
	b.next = &c;
	c.next = &d;
	d.next = &e;
	e.next = 0;
	ListNode *ret = sol.sortList(&a);
	printList(ret);
	cout << endl;
	return 0;
}