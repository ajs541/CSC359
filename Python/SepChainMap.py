# Aaron Standefer (with help from Mark Smith)
from HashMap import HashMap
from UnsortedMap import UnsortedMap

class SepChainMap(HashMap):
    
    def __init__(self, capacity=None):
        
        super().__init__(capacity)
    # The _bucket_(items) are to ensure the HashMap functions calling to them run properly 
    def _bucket_getitem(self, key, index):
        
        if self._bucketArray[index]==None:
            raise KeyError()
        return self._bucketArray[index][key]
    # makes an unsortedmap inside of hashmap
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
        
    def __iter__(self):
        for bucket in self._bucketArray:
            if bucket is not None:
                for key in bucket:
                    yield key
    
    def __str__(self):
        arrayString = "{"
        i=0
        for key in self:
            value = self[key]
            arrayString += str(key) + ":" + str(value)
            i += 1
            if i == len(self):
                arrayString += "}"
            else:
                arrayString += ", "
        return arrayString
# tester stuff
if __name__ == "__main__":
    a = SepChainMap()
    a[1] = "hi"
    a[2] = "it cold"
    a[3] = "it ain't snowing anymore"
    print(a)