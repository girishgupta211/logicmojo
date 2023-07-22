# 23. Merge k Sorted Lists
# Hard
# 17.7K
# 634
# Companies
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.


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

def mergeTwoSortedRecursion(l1 , l2):
    result = None
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.val > l2.val:
        result = l2
        result.next = mergeTwoSortedRecursion(l1, l2.next)
    else:
        result = l1
        result.next = mergeTwoSortedRecursion(l1.next,l2)

    return result


def mergeTwoSortedLists(list1, list2):
    new_list = ListNode(-1)
    ans_list = new_list

    while list1 is not None and list2 is not None:
        if list1.val > list2.val:
            new_list.next = ListNode(list2.val)
            
            list2 = list2.next 
        else:
            new_list.next = ListNode(list1.val)
            list1 = list1.next

        new_list = new_list.next
    while list1 is not None:
        new_list.next = ListNode(list1.val)
        new_list = new_list.next
        list1 = list1.next
    
    while list2 is not None:
        new_list.next = ListNode(list2.val)
        new_list = new_list.next
        list2 = list2.next

    return ans_list.next

def mergeKLists(lists):
    if len(lists) == 0:
        return []
    index = 1
    first_list = lists[0]
    while index < len(lists):
        first_list = mergeTwoSortedLists(first_list, lists[index])
        index += 1
    return first_list
    # printList(first_list)

list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# printList(head)
# printList(mergeTwoSortedLists(list1, list2))
# printList(mergeTwoSortedRecursion(list1, list2))


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)
lists = [ list1, list2, list3 ]

result = mergeKLists(lists)
printList(result)
result = mergeKLists([[]])
result = mergeKLists([])

print(result)