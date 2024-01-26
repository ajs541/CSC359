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
def isBalanced(parentString):
    balance = 0
    if parentString == "":
        raise SyntaxError
    for i in parentString:
        if i == "(":
            balance += 1
        elif balance <= 0:
            return False
        else:
            balance -= 1
    return balance==0

exampleString = ")()"
print(isBalanced(exampleString))
    