from ctypes import py_object

class List:

    def __init__(self, capacity=None):
        if capacity==None or capacity<10:
            self.__capacity = 10
        else:
            self.__capacity=capacity
        self.__arr = (self.__capacity*py_object)()

        self.__count=0
    
    def __len__(self):
        return self.__count
    
    def __getitem__(self, index):
        if self.__isValidIndex(index):
            return self.__arr[index]
        raise IndexError()
    
    def isValidIndex(self, i):
        if i<0 or i>=self.__count:
            return False
        return True
    
    
