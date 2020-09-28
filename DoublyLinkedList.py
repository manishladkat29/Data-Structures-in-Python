
class Node:
    
    def __init__(self, data):
         self.next = None
         self.prev = None
         self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push(self, new_data):   # Push an element to the start of the list
        new_node = Node(new_data)
        new_node.next = self.head
        
        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1


    def insertAfter(self, node_element, new_data): # Insert an element after the given node
        ptr = self.head
        new_node = Node(new_data)
        while ptr.data is not node_element:
            ptr = ptr.next
            if ptr is None:
                print("Element not found")
                return
        if ptr.next is None:
            ptr.next = new_node
            new_node.prev = ptr
            self.tail = new_node
            self.size += 1
            return
        ptr.next.prev = new_node
        new_node.next = ptr.next
        ptr.next = new_node
        new_node.prev = ptr
        self.size += 1
        
    def append(self, new_data): # Add an element to the end of the list
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        last = self.head
        while last.next is not None:
            last = last.next
        
        last.next = new_node
        new_node.prev = last
        self.tail = new_node
        self.size += 1

    def remove(self, element):  # Remove an element from the list
        ptr = self.head
        if self.head is None:
            print("Empty list element not found")
            return
        if self.head.data is element:
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1
            return
        while ptr.data is not element:
            ptr = ptr.next
            if ptr is None:
                print("Element not found")
                return
        if ptr.next is None:
            ptr.prev.next = None
            self.tail = ptr.prev
            self.size -= 1
            return
        ptr.prev.next = ptr.next
        ptr.next.prev = ptr.prev
        self.size -= 1    
        

    def printList(self):    # Print the list starting from the head node
        print("Linked List")
        ptr = self.head
        while ptr.next is not None:
            print(ptr.data, sep= " ")
            ptr = ptr.next
        print(ptr.data, self.head.data, self.tail.data, self.size)

dlist = DoublyLinkedList()
dlist.push(5)
dlist.insertAfter(5, 1)
dlist.append(9)
dlist.insertAfter(1, 2)
dlist.insertAfter(9, 10)
dlist.printList()
dlist.remove(10)
dlist.printList()

