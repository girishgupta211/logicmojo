# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:

# Given n will always be valid.

# Follow up:

# Could you do this in one pass?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head):
    temp = head
    while temp is not None:
        print(temp.val)
        temp = temp.next


def removeNthFromEnd(head, n):

    # Add a dummy node to remove first node from list
    # in the last return head.next
    dummy_node = ListNode(-1)
    dummy_node.next = head
    head = dummy_node

    slow = head

    # This will move n nodes in advance so that 
    fast = head

    while fast.next is not None and n > 0:
        fast = fast.next
        n -= 1
    
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    # printList(head.next)
    return head.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# printList(head)
removeNthFromEnd(head, 5)


# 0->1->2->3->4->5->6->7
# if I want to remove n=2 (6), then move slow pointer to 5
# if I want to remove n=1 (7), then move slow pointer to 6
# if I want to remove n=6 (2), then move slow pointer to 1

# Special case
# If number of nodes is equal to n, then , remove first node.
# head = head.next

# if I want to remove n=7 (1), then move slow pointer to 1

# take slow pointer and fast pointer 
# Move fast poiter n points from beginning 
# 1->2->3->4->5->6->7
# if I want to remove n=2 (6), then move slow pointer to 5
# fast will point to 3
# Then move both fast and slow till fast.next is not None
