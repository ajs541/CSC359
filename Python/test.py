"""
print("Hello World!")

print(5+2)

finish = False
i = 0
while not finish:
    if i > 10:
        print(i)
        finish = True
    elif i > -1 and i < 11:
        i = i+1
        print(i)
    else:
        i = 0
"""
import math
def moveZeroesLeft(list):
    zeroList = []
    otherList = []
    for i in range(len(list)):
        if list[i] == 0:
            zeroList.append(list[i])
        else:
            otherList.append(list[i])
    return zeroList + otherList

def distinctInts(list):
    exists = []
    for i in range(len(list)):
        if list[i] not in exists:
            print(list[i])
            exists.append(list[i])

def leftRightTriangle(int):
    if int <= 0:
        raise ValueError("cannot make a zero or negative triangle")
    count = 0
    for i in range(int):
        stars = ""
        for j in range(count+1):
            stars += "* "
        print(stars)
        count += 1

def rightRightTriangle(int):
    if int <= 0:
        raise ValueError("no empty triangles")
    count = int-1
    for i in range(int):
        stars = "  " *count
        stars += " *" *(int-count)
        print(stars)
        count -= 1
        
def isPalindrome(string):
    stringStack = []
    n = len(string)
    if 1==((-1)**n):
        isEven = True
    else:
        isEven = False
    if isEven == True:
        for i in range(n/2):
            stringStack.append(string[i])
        for j in range(n/2, n):
            if string[j] == stringStack.peek():
                stringStack.pop()
                if j == n:
                    return True
            else:
                return False
    else:
        for i in range(math.floor(n/2)):
            stringStack.append(string[i])
        for j in range(math.floor(n/2)+2, n):
            if string[j] == stringStack.peek():
                stringStack.pop()
                if j == n:
                    return True
            else:
                return False
    
def intSum(list, k):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == k:
                print([list[i], list[j]])
                return True
    return False



if __name__ in "__main__":
    ints = [4, 7, 2, 0, 3]
    sum = 5
    print(intSum(ints, sum))