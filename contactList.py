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
        print("The email you entered is " + contact.getEmail() + "'s email." + " Enter a different email")
        return True
      
    return False
      
contact1 = Contact("Alex", 123456789)
contact2 = Contact("Sarah", 123456786)
business1 = BusinessContact("Max", 123456783, "max@gmail.com", "Meta")
business2 = BusinessContact("Max", 123426783, "max@gmail.com", "Meta")
# contact3 = Contact("Alex", 123456787)

list = ContactList()
list.addContact(contact1)
list.addContact(contact2)
list.addContact(business1)
list.addContact(business2)

list.display()
