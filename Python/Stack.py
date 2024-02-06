class Stack:
    
    def __init__ (self, cap = None):
        self.__arr = []
        if cap is None or cap <= 0:
            self.__capacity = 1000
        else:
            self.__capacity = cap
    
    def push(self, element):
        if self.__capacity <= len(self.__arr):
            raise OverflowError("Stack is too large")
        self.__arr.append(element)
        
    def pop(self):
        if len(self.__arr)<=0:
            raise Exception("Stack is too small")
        return self.__arr.pop()
    
    def peek(self):
        if len(self.__arr)<=0:
            raise Exception("Stack is too small")
        return self.__arr[-1]
    