#!/usr/bin/env python3
'''
You’re given the pointer to the head nodes of two sorted linked lists.
The data in both lists will be sorted in ascending order. 
Change the next pointers to obtain a single, merged linked list 
which also has data in ascending order. Either head pointer given 
may be null meaning that the corresponding list is empty.

Some use deque insead of linkedlist
deque (pronounced “deck”), which stands for double-ended queue.
    #from collections import deque
create an empty linked list
    #deque() #deque.pop(); deque.popleft(); deque.append()
    #deque([])
    #llist1 = deque([{'data': '1'}, {'data': '3'}])
    #llist2 = deque([{'data': '2'}, {'data': '6'}, {'data': '7'}])
    method on linklist called sorted and throws an error if not
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __init__(self, nodes=None): #simplified way to load a linkedlist
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
    '''
    def __repr__(self):
        return str(self.data)
    '''
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def merge(self, l2):
        # Keep the first list; Iter over the second;
        # When second < first, insert second data into first list.
        l1 = self
        prev = None
        cur = l1.head
        other = l2.head
        while cur != None and other != None:
            if other.data == cur.data:
                prev = cur
                cur = cur.next
                continue
            if other.data < cur.data and other.data != cur.data:
                # hold current other before it changes
                otherNext = other.next
                if prev == None:
                    l1.head = other
                else:
                    prev.next = other
                # New other becomes the current
                other.next = cur
                prev = other
                other = otherNext
            else:
                # continue
                prev = cur
                cur = cur.next

        if other != None:
            if prev == None:
                l1.head = other
            else:
                prev.next = other

        # Reset l2 because we took all of its nodes
        l2.head = None
                    
        return l1
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def last_node(self) -> Node:
        node = self.head
        while node and node.next:
            node = node.next
        return node
    
    def index_of(self, target: Node) -> int:
        idx = 0
        node = self.head
        while node:
            if node == target:
                return idx
            idx = idx + 1
            node = node.next
        return -1
    
    def get_node(self, idx: int) -> Node:
        node = self.head
        while node and idx > 0:
           idx = idx - 1
           node = node.next
        return node 
        
    def detectCycle(self) -> Node:
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None


def buildLoopList(l1: LinkedList, index: int) -> LinkedList:
    # test full circle loop
    end = l1.last_node()
    end.next = l1.get_node(index)
    return l1   
   



# to call script directly
if __name__ == "__main__":
    
    llist1 = LinkedList([2, 3, 6, 7])
    llist2 = LinkedList([1, 4, 6, 11])
    
    #merge two LinkeLists into one LinkedList with no duplicates.
    #mergedlist = LinkedList.merge(llist1, llist2)

    # Purposely create a loop for testing
    try:
        llist3 = buildLoopList(LinkedList([1,2,3,4,5]), 3)
        loops_start = LinkedList.detectCycle(llist3)
        print(llist3.index_of(loops_start))
    except ValueError as e:
        print(f"ERROR: {e}")
        exit

    
    #print(f"Has loop? {LinkedList.detectCycle(mergedlist)}")
    #print("data in merged linklist:")
    #for node in mergedlist:
        #print(node.data)