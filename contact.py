class Contact:
  def __init__(self, name, number):
    self.__name = name #private variables
    if len(str(number)) != 9:
      print(name + "'s number is not valid. Try again.")
    else:
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
      



