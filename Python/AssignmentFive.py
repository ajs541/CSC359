# Aaron Standefer (with help from Mark Smith)
import math
from UnsortedMap import UnsortedMap
from Stack import Stack
#for question one, dictionary is very mutable,
#and sorted("string") => ['s', 't', 'r', 'i', 'n', 'g']
def anagramDetect(lst):
    letters = UnsortedMap()
    sort = sorted(lst[0])
    for i in range(len(sort)):
        if letters.get(sort[i]) != None:
            letters[sort[i]] = letters[sort[i]] + 1
        else:
            letters[sort[i]] = 1
    print(letters)

def mergeSortLists(list1, list2):
    newList = []
    count = 0
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            if count == 0:
                newList.append(list1[i])
                count += 1
                i += 1
                j += 1
            elif newList.__contains__(list1[i]) == False:
                newList.append(list1[i])
                count += 1
                i += 1
                j += 1
        elif list1[i] < list2[j]:
            if newList.__contains__(list1[i]) == False:
                newList.append(list1[i])
                count += 1
                i += 1
        elif list2[j] < list1[i]:
            if newList.__contains__(list2[j]) == False:
                newList.append(list2[j])
                count += 1
                j += 1
    if i == len(list1):
        i -= 1
    if j == len(list2):
        j -= 1
    if newList.__contains__(list1[i]) == False and list1[i] > list2[j]:
        newList.append(list1[i]) 
    if newList.__contains__(list2[j]) == False and list2[j] > list1[i]:
        newList.append(list2[j])                
    return newList

def bracketChecker(string):
    openStacker = Stack()
    for i in range(len(string)):
        tempChar = string[i]
        if i == 0:
            if tempChar == ">" or tempChar == ")" or tempChar == "]" or tempChar == "}":
                return False
        if tempChar == "<" or tempChar == "(" or tempChar == "[" or tempChar == "{":
            openStacker.push(tempChar)
        elif tempChar == ">":
            if openStacker.peek() == "<":
                openStacker.pop()
            else:
                return False
        elif tempChar == ")":
            if openStacker.peek() == "(":
                openStacker.pop()
            else:
                return False
        elif tempChar == "]":
            if openStacker.peek() == "[":
                openStacker.pop()
            else:
                return False
        elif tempChar == "}":
            if openStacker.peek() == "{":
                openStacker.pop()
            else:
                return False
        else:
            raise Exception()
    try:
        if openStacker.peek() is not None:
            return False
    except Exception:
        return True

def intOccur(lst):
    occur = UnsortedMap()
    for i in range(len(lst)):
        if occur.get(lst[i]) != None:
            occur[lst[i]] = occur[lst[i]] + 1
        else:
            occur[lst[i]] = 1
    print(occur)

def getPrimes(lst):
    primeList = []
    for i in range(len(lst)):
        isPrime = True
        if lst[i] == 1:
            isPrime = False
        if lst[i] > 1:
            for j in range(2, lst[i]):
                if (lst[i] % j) == 0:
                    isPrime = False
                    break
        if isPrime:
            primeList.append(lst[i])  
    if primeList == []:
        print("No primes")
        return None   
    print(primeList)
                    

if __name__ == "__main__":
    l2 = [7919, 7907, 7901, 7883, 7879, 7877, 7873, 7867, 7853, 7841, 7829, 7823, 7817, 7793, 7789, 7759, 7757, 7753, 7741, 7727, 2**82589933 - 1]
    l1 = [3, 9, 11, 14, 15, 25]
    l3 = [4, 6, 10]
    print(mergeSortLists(l1,l2))
    getPrimes(l2)
    l4 = [4, 6, 4, 10, 33, 10]
    intOccur(l4)
    l5 = ['act']
    anagramDetect(l5)
    l6 = '{(})<>[]'
    print(bracketChecker(l6))