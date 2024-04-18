from Stack import Stack
import math

def reverseString(string):
    stringStack = Stack()
    dnaDict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    i = 0
    while i < len(string):
        stringStack.push(string[i])
        i += 1
    final = ""
    while i != 0:
        final += dnaDict[stringStack.pop()]
        i-=1
    return final

if __name__ in "__main__":
    dna="ATGACCT"
    print(reverseString(dna))
    