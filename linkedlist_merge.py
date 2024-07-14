#!/usr/bin/env python3
'''
You’re given the pointer to the head nodes of two sorted linked lists.
The data in both lists will be sorted in ascending order. 
Change the next pointers to obtain a single, merged linked list 
which also has data in ascending order. Either head pointer given 
may be null meaning that the corresponding list is empty.
Some use deque insead of linkedlist
deque (pronounced “deck”), which stands for double-ended queue.
'''
#from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    

def mergeLists(l1, l2):
    dummy = LinkedList()
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next


# to call script directly
if __name__ == "__main__":
    #create an empty linked list
    #deque() #deque.pop(); deque.popleft(); deque.append()
    #deque([])
    #llist1 = deque([{'data': '1'}, {'data': '3'}])
    #llist2 = deque([{'data': '2'}, {'data': '6'}, {'data': '7'}])
    ''' Simple way to build linkedlist
    llist1 = LinkedList()
    llist2 = LinkedList()
    # build the first linkedlist
    first_node = Node("1")
    llist1.head = first_node
    second_node = Node("3")
    first_node.next = second_node
    third_node = Node("5")
    second_node.next = third_node
    # make second linkedlist
    first_node = Node("2")
    llist2.head = first_node
    second_node = Node("4")
    first_node.next = second_node
    third_node = Node("9")
    second_node.next = third_node
    '''
    llist1 = LinkedList(["1", "3", "5", "7"])
    llist2 = LinkedList(["2", "4", "9", "11"])

    mergedlist = mergeLists(llist1, llist2)
    for node in mergedlist:
        print(node)
   