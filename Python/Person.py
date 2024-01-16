class Person:
    
    def __init__(self, fname, lname, email, city, idNumber, phoneNumber):
        self.__firstName = fname
        self.__lastName = lname
        self.__email = email
        self.__city = city
        self.__idNumber = idNumber
        self.__phoneNumber = phoneNumber
    
    def getFirstName(self):
        return self.__firstName
    
    def setFirstName(self, newFname):
        self.__firstName = newFname

    def getLastName(self):
        return self.__lastName
    
    def setLastName(self, newLname):
        self.__lastName = newLname
    
    def getEmail(self):
        return self.__email
    
    def setEmail(self, newEmail):
        self.__email = newEmail
    
    def getCity(self):
        return self.__city
    
    def setCity(self, newCity):
        self.__city = newCity
    
    def getIdNumber(self):
        return self.__idNumber
    
    def setIdNumber(self, newIdNumber):
        self.__idNumber = newIdNumber

    def getPhoneNumber(self):
        return self.__phoneNumber
    
    def setPhoneNumber(self, newPhoneNumber):
        self.__phoneNumber = newPhoneNumber
    