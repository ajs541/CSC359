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

class Person:

    def __init__ (self, fname, lname, email, city):
        self.__firstName = fname
        self.__lastName = lname
        self.__email = email
        self.__city = city
    
    def getFirstName(self):
        return self.__firstName
    
    def setFirstName(self, newFname):
        self.__firstName = newFname
    
    def printMessage(self):
        print("This is a message for the sake of a message!")
    
p1 = Person('Aaron', 'Standefer', 'astandefer24', 'Cedar Rapids')
firstName = p1.getFirstName()

p1.setFirstName("Josh")

print(f'previous first name = {firstName}')
print(f'new first name is ')