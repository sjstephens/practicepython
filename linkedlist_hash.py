#!/usr/bin/env python3
'''
Traverse the list individually and keep putting the node addresses in a Hash Table. 
At any point, if NULL is reached then return false 
If the next of the current nodes points to any of the previously 
stored nodes in Hash then return true.
'''

# Node class
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None
        self.flag = 0

# Node class
class Node:

    # Constructor to initialize
    # the node object
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new
    # node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print it
    # the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def detectLoop(self):
        s = set()
        temp = self.head
        while (temp):

            # If we already have
            # this node in hashmap it
            # means there is a cycle
            if (temp in s):
                return True

            # If we are seeing the node for
            # the first time, insert it in hash
            s.add(temp)

            temp = temp.next

        return False


# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

if(llist.detectLoop()):
    print("Loop Found")
else:
    print("No Loop ")