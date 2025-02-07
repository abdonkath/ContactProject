class Contact:
  def __init__(self, name, number):
    self.__name = name #private variables
    self.__number = number  #private variables
    
  #Encapsulation - private variables so that it cannot be access directly
  #getters
  def getName(self):
      return self.__name
    
  def getNumber(self):
      return self.__number
    
  #setters
  def changeName(self, name):
      self.__name = name
      
  def changeNumber(self, number):
      self.__number = number

class BusinessContact(Contact): #Inheritance
  def __init__(self, name, number, email, company):
     super().__init__(name, number)
     self.__email = email
     self.__company = company
  
  #getters
  def getEmail(self):
    return self.__email
  
  def getCompany(self):
    return self.__company
  
  #setters
  def changeEmail(self, email):
    self.__email = email
    
  def changeCompany(self, company):
    self.__company = company
    
     
  


