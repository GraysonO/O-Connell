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

    def Merge_Lists(self,x,y):
        y.element.next = x.element

