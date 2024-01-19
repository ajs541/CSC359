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
    
    def __setitem__(self, index, element):
        if not self.__isValidIndex(index):
            raise IndexError()
        self.__arr[index]=element
    
    def __isValidIndex(self, i):
        if i<0 or i>=self.__count:
            return False
        return True
    
    def _resize(self, newCap):
        temp = self.__arr
        self.__arr = (newCap*py_object)()
        for i in range(0, self.__count):
            self.__arr[i]=temp[i]
        self.__capacity = newCap
    
    def append(self, element):
        if self.__count == self.__capacity:
            self._rezie(self.__capactiy*2)
        self.__arr[self.__count]=element
        self.__count += 1

    def insert(self, index, element):
        if not self.__isValidIndex(index):
            raise IndexError()
        if self.__count == self.__capacity:
            self._resize(self.__capacity*2)
        for i in range(self.__count-1, index-1, -1):
            self.__arr[i+1]=self.__arr[i]
        self.__arr[index]=element
        self.__count+=1

    def __iter__(self):
        self.__index=0
        return self
    
    def __next__(self):
        if self.__index<self.__count:
            temp=self.__arr[self.__index]
            self.__index += 1
            return temp
        raise StopIteration()
    
    def __contains__(self, key):
        for i in range(0, self.__count):
            if key==self.__arr[i]:
                return True
        return False
    
    def pop(self, i=None):
        if i == None:
            i=self.__count-1
        if not self.__isValidIndex(i):
            raise IndexError()
        removeItem = self.__arr[i]
        for j in range(i, self.__count-1):
            self.__arr[j]=self.__arr[j+1]
        self.__count-=1
        return removeItem
    
    def remove(self, e):
        for i in range(0, self.__count):
            if self.__arr[i]==e:
                self.pop(i)
                return None
        raise ValueError("element does not exit")
