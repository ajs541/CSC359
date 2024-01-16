from Person import Person

class Faculty(Person):

    def __init__(self, firstName, lastName, email, city, idNumber, phoneNumber, department, designation, officeLocation):
        super().__init__(firstName, lastName, email, city, idNumber, phoneNumber)
        self.__department = department
        self.__designation = designation
        self.__officeLocation = officeLocation
    
    def getDepartment(self):
        return self.__department
    
    def setDepartment(self, newDepartment):
        self.__department = newDepartment
    
    def getDesignation(self):
        return self.__designation
    
    def setDesignation(self, newDesignation):
        self.__designation = newDesignation
    
    def getOfficeLocation(self):
        return self.__officeLocation
    
    def setOfficeLocation(self, newOfficeLocation):
        self.__officeLocation = newOfficeLocation
    
