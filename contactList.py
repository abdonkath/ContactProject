#container for contacts
#add contacts
#remove contacts
#sort contact alpabethically

from contact import Contact
from contact import BusinessContact

class ContactList:
  def __init__(self):
    self.contacts = [] #list 
  
  def addContact(self, contact):
    if not self.isValidNum(contact.getNumber()): # if the number given is not valid
      while True:
        num = input(contact.getName() + "'s number is not valid. Please enter a valid number: ")
        if self.isValidNum(num):
          contact.changeNumber(num)
          break
        
    if isinstance(contact, BusinessContact):
      if self.checkNumber(contact.getNumber()) or self.checkEmail(contact.getEmail()):
        return
    else:
      if self.checkNumber(contact.getNumber()):
        return
    self.contacts.append(contact)
  
  def removeContact(self, name):
    same_name = [contact for contact in self.contacts if contact.getName() == name] #comprehension
    
    if len(same_name) > 1: #Checks if there is multiple number w/ the same name
      count = 0
      for contact in same_name:
        count += 1
        if isinstance (contact, BusinessContact):
          print(str(count) + ") " + str(contact.getName()) + " #" + str(contact.getNumber()) + " " + str(contact.getEmail()) + " (" + str(contact.getCompany()) + ")")
        else:
          print(str(count)+ ") " + str(contact.getName()) + " #" + str(contact.getNumber()))
        
      choice = int(input("Which do you want to remove? ")) - 1
      self.contacts.remove(same_name[choice]) #removes the index that the user input
    else:
      self.contacts.remove(same_name[0]) #if there is no same names then there should be only one element in the list, so it will be remove
      
  def display(self):
    for c in self.contacts:
      if isinstance (c, BusinessContact):
        print(str(c.getName()) + " #" + str(c.getNumber()) + " " + str(c.getEmail()) + " (" + str(c.getCompany()) + ")")
      else:
        print(str(c.getName()) + " #" + str(c.getNumber()))
        
  #check if the number is valid 
  def isValidNum(self, number):
    if len(str(number)) != 9:
      return False
    return True
  
  #What if a phone number is already in the system?
  #This function will check if the contact being added is already in the system
  def checkNumber(self, number):
    for contact in self.contacts:
      if contact.getNumber() == number:
        print("The number you entered is " + contact.getName() + "'s number." + " Enter a different number")
        return True
      
    return False
  
  #What if the email is already in the system?
  #This function will check if the email being added is already in the system
  def checkEmail(self, email):
    for contact in self.contacts:
      if isinstance(contact, BusinessContact) and contact.getEmail() == email:
        print("The email you entered is already in the system. Enter a different email")
        return True
      
    return False
      
contact1 = Contact("Alex", 12345689)

list1 = ContactList()
list1.addContact(contact1)

list1.display()
