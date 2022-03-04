#!/usr/bin/python

import collections

# Note: collections.deque is the built in Linked List type in python


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    # Some python magic to prettily print linked lists.
    def __str__(self):
        if self.next:
            return f"[{self.data} ->] {str(self.next)} "
        else:
            return f"[{self.data} ->]"


def linked_list_from_array(iterable):
    if not iterable:
        return None
    head = None
    first = True
    for data in iterable:
        if first:
            current = Node(data)
            head = current
            first = False
        else:
            current.next = Node(data)
            current = current.next
    return head

# Guidelines on speed of linked list operations
# best case iteration is O(n)
# best case insertion is O(1) (neat!!!)


"""
Reverse a LinkedList:

Write a function that takes the head of a linkedlist, reverses it and returns 
  the new head.
Assume the head will never be null

Example: input => 1->2->3->4->5 | output => 5->4->3->2->1

input head is [1-> Node(2)]
output head to be [5 -> Node(4)] ...
"""


def reverse_linked_list(head):
    # we need to traverse, so can we? Can we just print 1,2,3,4,5?
    current_pointer = head  # head is not null

    tmp_pointer = None
    while current_pointer is not None:
        print(current_pointer.data)
        next_pointer = current_pointer.next
        current_pointer.next = tmp_pointer
        tmp_pointer = current_pointer
        current_pointer = next_pointer  # i = i +1 for linked lists
    return tmp_pointer


"""
Find the Loop:

Given a linkedlist, identify whether it has a loop or not. If it does, return the data of the node
at the start of the loop. If it does not, return null

Example: input => 1->2->3->4->5->3 | output => 3
Example: input => 1->2->3->4->5->6 | output => null
"""


def find_loop(head):
    if head is None:
        return None

    slow_pointer = head
    fast_pointer = head

    # figure out if there is a loop or not
    #                                  v - two more nodes left to go (at least)
    while fast_pointer is not None and fast_pointer.next is not None:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
        if slow_pointer == fast_pointer:
            print("found a pointer match")
            break
    if fast_pointer is None:
        return None
    if fast_pointer.next is None:
        return None

    # Then "search" for where they meet:
    slow_pointer = head
    while slow_pointer != fast_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    return fast_pointer


if __name__ == "__main__":
    if False:
        x = linked_list_from_array([1, 2, 3, 4, 5])
        print("input", x)
        reversed_x = reverse_linked_list(x)
        print("\nreversed: ")
        print(reversed_x)
