from .linkedList import SingleLinkedList



lista1 = SingleLinkedList()
lista2 = SingleLinkedList()

lista1.appendToTail(1)
lista1.appendToTail(2)
lista1.appendToTail(4)
lista1.appendToTail(6)


lista2.appendToTail(2)
lista2.appendToTail(3)
lista2.appendToTail(5)



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1:[SingleLinkedList], list2: [SingleLinkedList]) -> [SingleLinkedList]:

        aux = SingleLinkedList(-1)
        current: SingleLinkedList = aux
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if not list1:
            current.next = list2
        else:
            current.next = list1

        return aux.next


    """
    1 -> 2 -> 4 -> 6 LIST 1
    2 -> 3 -> 5  LIST 2
    OUTPUT = 1 -> 2 -> 2 -> 3 -> 4 -> 5 -> 6

    (AUX Y CURRENT TIENEN LO MSIMO DE REFERENCIA)
    1er iteracion
    [-1] aux
    [-1] current
    [-1, 1 ] current
    
    cuando list1 o list2 no tengan nada se pasa directamente a la otra lista
    si ninguna de las dos tienen ningun valor mas, es xq llegamos al final, retornamos el aux.next
    o sea sin el -1
    """