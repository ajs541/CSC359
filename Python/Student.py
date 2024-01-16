from Person import Person

class Student(Person):

    def __init__(self, firstName, lastName, email, city, idNumber, phoneNumber, major, gradYear, gpa):
        super().__init__(firstName, lastName, email, city, idNumber, phoneNumber)
        self.__major = major
        self.__gradYear = gradYear
        self.__gpa = gpa
    
    def getMajor(self):
        return self.__major
    
    def setMajor(self, newMajor):
        self.__major = newMajor
    
    def getGradYear(self):
        return self.__gradYear
    
    def setGradYear(self, newGradYear):
        self.__gradYear = newGradYear
    
    def getGpa(self):
        return self.__gpa
    
    def setGpa(self, newGpa):
        self.__gpa = newGpa
    