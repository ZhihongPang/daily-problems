"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""
# research for the problem
# constant space complexity means the memory/space used by the program is independent of the input size
# O(M + N) time suggests two independent loops, one for each list
# rules: assume nodes of the same value to be the same node objects
#        create linked list data structure in python

import unittest

# assumes intersection exists
class Node:
    def __init__(self, data=None) -> None:
        self._data = data if data else None
        self._next = None
    def __str__(self) -> str:
        return str(self._data)

# O(m) + O(n) + O(m - n) + O(m)|O(n) = O(2m + n) = O(m + n)
# constant space complexity
def find_intersection(listA : Node, listB : Node) -> Node:
    currA, currB = listA, listB
    lenA, lenB = 0, 0
    while currA._next != None: # O(m)
        lenA += 1
        currA = currA._next
    while currB._next != None: # O(n)
        lenB += 1
        currB = currB._next

    currA, currB = listA, listB
    delta = lenA - lenB
    for _ in range(abs(delta)): # O(m - n)
        if delta > 0:
            if currA._data == currB._data:
                return currA
            currA = currA._next
        if delta < 0:
            if currA._data == currB._data:
                return currB
            currB = currB._next
    delta = lenA if lenA >= lenB else lenB
    for _ in range(delta): # O(m)/O(n)
        if currA._data == currB._data:
            return currA
        currA, currB = currA._next, currB._next
    return Node() # empty node indicate non-intersection
    
def print_linked_list(linked_list) -> None:
    curr = linked_list
    while curr._next != None:
        print(curr)
        curr = curr._next
    
class Test(unittest.TestCase):
    def test_given(self):
        listA, listB = [3, 7, 8, 10], [99, 1, 8, 10]
        linked_listA, linked_listB = Node(listA[0]), Node(listB[0])
        currA, currB = linked_listA, linked_listB
        for _ in range(1, len(listA)): # only works if listA and listB are the same length
            currA._next, currB._next = Node(listA[_]), Node(listB[_])
            currA, currB = currA._next, currB._next
        self.assertEqual(find_intersection(linked_listA, linked_listB)._data, 8)
    def test_uneven_lists(self):
        listA, listB = [2, 3, 4, 5, 6, 7, 8, 10], [99, 1, 8, 10]
        linked_listA, linked_listB = Node(listA[0]), Node(listB[0])
        currA, currB = linked_listA, linked_listB
        for _ in range(1, len(listA)):
            currA._next= Node(listA[_])
            currA = currA._next
        for _ in range(1, len(listB)):
            currB._next = Node(listB[_])
            currB = currB._next
        self.assertEqual(find_intersection(linked_listA, linked_listB)._data, 8)
    def test_early_intersection(self):
        listA, listB = [1, 2, 3, 4, 5, 6, 7], [1, 2, 3]
        linked_listA, linked_listB = Node(listA[0]), Node(listB[0])
        currA, currB = linked_listA, linked_listB
        for _ in range(1, len(listA)):
            currA._next= Node(listA[_])
            currA = currA._next
        for _ in range(1, len(listB)):
            currB._next = Node(listB[_])
            currB = currB._next
        self.assertEqual(find_intersection(linked_listA, linked_listB)._data, 1)
if __name__ == "__main__":
    unittest.main()

        
