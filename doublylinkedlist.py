# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.val == other.val


myset = set()
myset.add(12)

nod1 = ListNode(12)
nod2 = ListNode(12)
print(nod2 == nod1)
