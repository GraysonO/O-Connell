class LinkedStack:

    class Node:
        slots = '_element', '_next'

        def init (self, element, next):
            self.element = element
            self.next = next

    def init (self):
        self.head = None
        self.size = 0

    def len (self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self.head = self.Node(e,self.head)

    def top(self):
        if self.isempty():
            raise Empty('Stack is empty')
        return self.head.element

    def pop(self):
        if self.isempty():
            raise Empty('Stack is empty')
        answer = self.head.element
        self.head = self.head.next
        self.size -= 1
        return answer

    def Sort(self,x,y):
        sorted = LinkedStack
        if x.head >= y.head:
            sorted.head = x.head
        else:
            sorted.head = y.head
        while x.next != None and y.next != None:
            if x.next < y.next:
                sorted.next = y.next
            else:
                sorted.next = x.next

a = LinkedStack()
a.push(3)
a.push(5)
a.push(7)

b = LinkedStack()
b.push(2)
b.push(3)
b.push(4)

c = LinkedStack
c.Sort(a,b)
print c
