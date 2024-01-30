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
        

if __name__ in "__main__":
    L = [3, 0, 4, 6, 0, 3]
    leftRightTriangle(4)
    rightRightTriangle(4)