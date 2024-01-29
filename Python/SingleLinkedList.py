from Node import Node

class SingleLinkedList:
    
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
    
    def addFirst(self, element):
        newNode = Node(element)
        if self.__count == 0:
            self.__tail = newNode
        else:
            newNode.next = head
        head = newNode
        self.__count += 1
    
    def addLast(self, element):
        newNode = Node(element)
        if self.__count == 0:
            self.__head = newNode
        else:
            self.__tail.next = newNode
        self.__tail = newNode
        self.__count += 1
    
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
        
    def removeFirst(self):
        if self.__count == 0:
            raise Exception("Cannot remove element from empty list")
        element = self.__head.data
        if self.__count == 1:
            self.__tail = None
        self.__head = self.__head.next
        self.__count += 1
        return element
    
    def removeLast(self):
        if self.__count == 0:
            raise Exception("Cannot remove element from empty list")
        