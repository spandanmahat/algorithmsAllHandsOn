class Stack:
    def __init__(self, size):
        self.top = 0
        self.size = size
        self.S = [0] * size


    def stack_empty(self):
        if self.top == 0:
            return True
        else:
            return False


    def push(self, x):
        if self.top == self.size:
            raise Exception("Stack Overflow")
        self.S[self.top] = x
        self.top += 1

    def pop(self):
        if self.stack_empty():
            raise Exception("Underflow")
        self.top -= 1
        return self.S[self.top]




class Queue:
    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.length = size
        self.Q = [0] * size

    def enqueue(self, x):
        self.Q[self.tail] = x
        if self.tail == self.length - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        x = self.Q[self.head]
        if self.head == self.length - 1:
            self.head = 0
        else:
            self.head += 1
        return x



#singly linkedlist
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def list_search(self, k):
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def list_insert(self, x):
        x.next = self.head
        self.head = x

    def list_delete(self, x):
        if self.head is None:
            return
        if self.head == x:
            self.head = x.next
            return

        temp = self.head
        while temp.next is not None and temp.next != x:
            temp = temp.next
        if temp.next == x:
            temp.next = x.next



# Invoking the algorithms
print("For stack implementation:")
S = Stack(5)
S.push(12)
S.push(25)
print(S.pop())  # Output: 25

print("\nFor queue implementation:")
Q = Queue(5)
Q.enqueue(10)
Q.enqueue(20)
print(Q.dequeue())  # Output: 10

print("\nFor linkedlist implementation:")
L = LinkedList()
node1 = ListNode(33)
node2 = ListNode(55)
L.list_insert(node1)
L.list_insert(node2)
searched_node = L.list_search(33)

# Output should be: 33
if searched_node:
    print(searched_node.key)
else:
    print("Not found")


L.list_delete(node1)
searched_node = L.list_search(33)


# Output should be: "Not found"
if searched_node:
    print(searched_node.key)
else:
    print("Not found")