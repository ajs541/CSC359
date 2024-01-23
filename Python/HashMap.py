from BaseMap import BaseMap

class HashMap(BaseMap):
    
    def __init__(self, capacity=None):
        
        super().__init__()
        self._bucketArray = [None] * self.__capacity
        if capacity == None:
            self.__capacity=11
        else:
            self.__capacity=capacity
        self._count=0
        self.__prime=16937
        self.__scale=277
        self.__offset=1033
    
    def __len__(self):
        
        return self._count
    
    def __hashFunction(self, key):
        
        h=hash(key)
        index = (((h*self.__scale)+self.__offset)%self.__prime)%self.__capacity
        return index
    
    def __setitem__(self, key, value):
        
        index=self.__hashFunction(key)
        self._bucket_setitem(key, value, index)
    
    def __delitem__(self,key):
        
        index = self.__hashFunction(key)
        self._bucket_delitem(key, index)
        
    