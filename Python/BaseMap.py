#Aaron Standefer
from _collections_abc import MutableMapping

class BaseMap(MutableMapping):
    # This class sets up so =, <. !=. and > are set to work with map functions
    class Item:
        
        def __init__(self, k, v):
            
            self.key=k
            self.value=v
            
        def __eq__(self,other):
            
            return self.key==other.key
        
        def __lt__(self,other):
            
            return self.key<other.key
        
        def __ne__(self,other):
            
            return self.key != other.key
        
        def __gt__(self,other):
            
            return self.key>other.key
        
        