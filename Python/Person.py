class Person:
    
    def __init__(self, fname, lname, email, city):
        self.__firstName = fname
        self.__lastName = lname
        self.__email = email
        self.__city = city
    
    def getFirstName(self):
        return self.__firstName
    
    def setFirstName(self, newFname):
        self.__firstName = newFname
    
    