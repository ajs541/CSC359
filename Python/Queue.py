
class Queue:
    
    def __init__(self):
        self.__arr=[None]*10
        self.__front= -1
        self.__rear= -1
        
    def enqueue(self, element):
        
        if self.__front==-1:
            self.__front=0
        elif self.__isFull():
            self.__resize(2*len(self.__arr))
        self.__rear=(self.__rear+1) % len(self.__arr)
        self.__arr[self.__rear] = element
        
    def dequeue(self):
        
        if self.isEmpty():
            raise Exception()
        temp = self.__arr[self.__front]
        self.__front = (self.__front + 1) % len(self.__arr)
        if self.isEmpty():
            self.__front = self.__rear = -1
        if (len(self.__arr) // 2) > 10 and len(self) < len(self.__arr) // 4:
            self.__resize(len(self) // 2)
        return temp
        
    def isEmpty(self):
        
        return self.__front == -1
    
    def __isFull(self):
        
        return len(self) == len(self.__arr)
    
    def __len__(self):
        
        if self.__front == -1:
            return 0
        return ((self.__rear + len(self.__arr) - self.__front) % len(self.__arr)) + 1
    
    def __str__(self):
        
        return str(list(self))
    
    def __resize(self, capacity):
        newArray = [None]*capacity
        for i, element in enumerate(self):
            newArray[i] = element
        self.__arr = newArray
        self.__front = 0
        self.__rear = i
        
        
    
    def __iter__(self):
        pointer = self.__front
        while pointer != self.__rear:
            yield self.__arr[pointer]
            pointer=(pointer+1) % len(self.__arr)
        yield self.__arr[pointer]
        
        
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(6)
    #print(q.__isFull())
    print(q)