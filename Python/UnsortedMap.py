# Aaron Standefer (with help from Mark Smith)
from BaseMap import BaseMap

class UnsortedMap(BaseMap):
    
    def __init__(self):
        
        self.__items: list[BaseMap.Item]= []
        
    def __len__(self):
        
        return len(self.__items)
    
    def __getitem__(self,key):
        
        for item in self.__items:
            
            if item.key==key:
                
                return item.value
            
        raise KeyError("Key does not exist")
    
    def __setitem__(self,key,value):
        
        found = False
        
        for item in self.__items:
            
            if item.key==key:
                
                item.value=value
                found=True
                
        if not found:
            
            item=self.Item(key,value)
            self.__items.append(item)
            
    def __delitem__(self,key):
        
        index = None
        
        for i in range(len(self.__items)):
            
            if key==self.__items[i].key:
                
                index=i
            
        if index != None:
            
            self.__items.pop(index)
            
        else:
            
            raise KeyError()
        
    def __iter__(self):
        
        self.__index=0
        return self
    
    def __next__(self):
        
        if self.__index >= len(self.__items):  
            raise StopIteration()
        key = self.__items[self.__index].key
        self.__index += 1
        return key
    
    def __str__(self):
        arrayString = "{"
        i=0
        for pair in self.__items:
            arrayString += str(pair.key) + ":" + str(pair.value)
            i += 1
            if i == len(self.__items):
                arrayString += "}"
            else:
                arrayString += ", "
        return arrayString


if __name__ == "__main__":
    a = UnsortedMap()
    a[1] = "hi"
    a[2] = "it cold"
    a[3] = "it ain't snowing anymore"
    print(a)