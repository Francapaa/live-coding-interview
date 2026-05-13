class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def appendToTail(self, value: int):
        if not self.head:
            self.head = Node(value)
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = Node(value)

    def deleteNode (self, value: int):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
        

        current: Node = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def print(self):
        if not self.head:
            print("END")
        
        current: Node = self.head

        while current.next:
            print("->", current.value)
            current = current.next
        print("END")




lista = SingleLinkedList()

lista.appendToTail(5)
lista.appendToTail(4)
lista.appendToTail(3)
lista.appendToTail(2)
lista.appendToTail(1)

lista.print()

lista.deleteNode(3)
lista.print()