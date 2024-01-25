
class Queue:
    
    def __init__(self):
        self.__arr=[None]*10
        self.__front= -1
        self.__rear= -1
        
    def enqueue(self, element):
        
        if self.__front==-1:
            self.__front=0
        elif (self.__rear + 1) % len(self.__arr) == self.__front:
            self.__resize(2*len(self.__arr))
        self.__rear=(self.__rear+1) % len(self.__arr)
        self.__arr[self.__rear] = element
        
    