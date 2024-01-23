from HashMap import HashMap
from UnsortedMap import UnsortedMap

class SepChainMap(HashMap):
    
    def __init__(self, capacity=None):
        
        super().__init__(capacity)
        
    def _bucket_getitem(self, key, index):
        
        if self._bucketArray[index]==None:
            raise KeyError()
        return self._bucketArray[index][key]
    
    def _bucket_setitem(self, key, value, index):
        
        if self._bucketArray[index]==None:
            self._bucketArray[index] = UnsortedMap()
        oldlen = len(self._bucketArray[index])
        self._bucketArray[index][key] = value
        newlen = len(self._bucketArray[index])
        self._count = self._count + (newlen - oldlen)
    
    def _bucket_delitem(self, key, index):
        
        if self._bucketArray[index]==None:
            raise KeyError()
        del self._bucketArray[index][key]
        self._count=self._count-1