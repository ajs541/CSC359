# Aaron Standefer (with help from Mark Smith)
# Put Node Class in same file since the class is only accessed here
class Node:
    
    def __init__(self, data, next=None):
        
        self.next = next
        self.data = data

class SingleLinkedList:
    # setting head and tail to point to None initially, count at 0
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
    # Checks if any entries in list, if so put element in entry one, otherwise initializes list with one entry
    def addFirst(self, element):
        newNode = Node(element)
        if self.__count == 0:
            self.__tail = newNode
        else:
            newNode.next = self.__head
        self.__head = newNode
        self.__count += 1
    # Same as above but adding to the end of the list
    def addLast(self, element):
        newNode = Node(element)
        if self.__count == 0:
            self.__head = newNode
        else:
            self.__tail.next = newNode
        self.__tail = newNode
        self.__count += 1
    # Takes the element and puts it at the position
    def add(self, pos, element):
        if pos == None or pos < 0 or pos > self.__count:
            raise Exception("Position of bounds")
        if pos == 0:
            self.addFirst(element)
        elif pos == self.__count:
            self.addLast(element)
        else:
            newNode = Node(element)
            temp = self.__head
            for _ in range(pos-1):
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
            self.__count += 1
    # Removes element and sets the element after it to head, raises error if list is empty
    def removeFirst(self):
        if self.__count == 0:
            raise Exception("Cannot remove element from empty list")
        element = self.__head.data
        if self.__count == 1:
            self.__tail = None
        self.__head = self.__head.next
        self.__count -= 1
        return element
    # like above but with tail, raises error if empty
    def removeLast(self):
        if self.__count == 0:
            raise Exception("Cannot remove element from empty list")
        element = self.__tail.data
        if self.__count == 1:
            self.__head = None
            self.__tail = None
        else:
            newTail = self.__at(self.__count - 2)
            newTail.next = None
            self.__tail = newTail
        self.__count -= 1
        return element
    # removes the element at position, raises error if empty
    def remove(self, pos):
        if self.__count == 0:
            raise Exception("Cannot remove element from empty list")
       # element = self.__at(pos).data
        if self.__count == 1:
            element = self.__head.data
            self.__head = None
            self.__tail = None
            self.__count -= 1
            return element
        if pos == 0:
            return self.removeFirst()
        if pos == self.__count:
            return self.removeLast()
        else:
            newPos = self.__at(pos-1)
            element = newPos.next.data
            newPos.next = newPos.next.next
            self.__count -= 1
            return element
    # returns element at position if the position exists in list
    def get(self, pos):
        if self.__count == 0:
            raise Exception("List is empty")
        return self.__at(pos).data
    # boolean for if list contains element
    def __contains__(self, data):
        
        current = self.__head
        while current != self.__tail:
            if current.data == data:
                return True
            current = current.next
        return False
    # repeatable function for going thru list to a set index, returning node at said index
    def __at(self, index):
        if index == None or index < 0 or index >= self.__count:
            raise Exception("Index not in bounds of list")
        current = self.__head
        for _ in range(index):
            current = current.next
        return current
    
    def __iter__(self):
        node = self.__head
        while node != self.__tail:
            yield node.data
            node = node.next
        yield node.data

if __name__ == "__main__":
    list = SingleLinkedList()
    list.addFirst(55)
    list.addLast(34)
    print(list.removeFirst())