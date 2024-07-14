#!/usr/bin/env python3
'''
Have a visited flag with each node.
Traverse the linked list and keep marking visited nodes.
If you see a visited node again then there is a loop.
'''
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None
        self.flag = 0


def push(head_ref, new_data):
    #allocate node and put in the data
    new_node = Node(new_data)

    new_node.flag = 0

    #link the old list of the new node
    new_node.next = (head_ref)

    #move the head to point to the new node
    (head_ref) = new_node
    return head_ref

# Returns true if there is a loop in linked list
# else returns false.


def detectLoop(h):

    while (h != None):
        # If this node is already traverse
        # it means there is a cycle
        if (h.flag == 1):
            return True

        # If we are seeing the node for
        # the first time, mark its flag as 1
        h.flag = 1
        h = h.next
    return False


''' Driver program to test above function'''
if __name__ == '__main__':

    ''' Start with the empty list '''
    head = None

    head = push(head, 20)
    head = push(head, 4)
    head = push(head, 15)
    head = push(head, 10)

    ''' Create a loop for testing '''
    head.next.next.next.next = head

    if (detectLoop(head)):
        print("Loop Found")
    else:
        print("No Loop")