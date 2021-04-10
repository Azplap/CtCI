"""
I really don't fuck w/ linkedlists but for now at least I will implement the
class for it. Come back to it later. Tbh it looks like it's not even any more
runtime efficient in python compared to normal lists. Either way important
to review this DS.

One thing to finally learn!!! --> Python Descriptors
What are Python Descriptors?
They are used in classes to give an objects special behaviors.
Ex: __init__ runs right when an object is created and for the case of
a "Person" class it will automatically assign a name to the object upon creation.

# init method or constructor   
def __init__(self, name):
    self.name = name


https://www.geeksforgeeks.org/__init__-in-python/
https://realpython.com/linked-lists-python/
"""
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return self.data
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

if __name__ == '__main__':
    llist = LinkedList(["a", "b", "c", "d", "e"])
    print(llist)
