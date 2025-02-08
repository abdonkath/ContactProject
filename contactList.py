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
    while not self.isValidNum(contact.getNumber()):  # Check if the number is valid initially
        num = input(contact.getName() + "'s number is not valid. Please enter a valid number: ")
        if self.isValidNum(num):
            contact.changeNumber(num)

    # Check if number already exists in the system
    while self.checkNumber(contact.getNumber()):
      print("The number you entered is already in use. Please enter a different number.")
      # Ask for a new number and validate
      num = input("Please enter a new valid number for " + contact.getName() + ": ")
      while not self.isValidNum(num):  # Keep prompting until the number is valid
        num = input(contact.getName() + "'s number is not valid. Please enter a valid number: ")
        contact.changeNumber(num)
        
        # If the contact is a BusinessContact, check email too
    if isinstance(contact, BusinessContact):
      while self.checkEmail(contact.getEmail()):  # Keep prompting until the email is not in use
        email = input("The email you entered for " + contact.getName() + " is already in use. Please enter a different email: ")
        contact.changeEmail(email)
    self.contacts.append(contact) #add the contact to list

  
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
    if len(str(number)) != 10:
      return False
    return True
  
  #What if a phone number is already in the system?
  #This function will check if the contact being added is already in the system
  def checkNumber(self, number):
    for contact in self.contacts:
      if contact.getNumber() == number:
        return True
      
    return False
  
  #What if the email is already in the system?
  #This function will check if the email being added is already in the system
  def checkEmail(self, email):
    for contact in self.contacts:
      if isinstance(contact, BusinessContact) and contact.getEmail() == email:
        return True
      
    return False
  
  def addNewContact(self):
    type_contact = input("What type of contact would you like to add?\n" + "a) Contact\n" + "b) Business Contact\n").lower()
    
    if (type_contact == 'a' or type_contact == "contact"):
      name = input("Enter a name: ")
      num = input("Enter a number: ")
      contact = Contact(name, num)
      self.addContact(contact)
    elif(type_contact == 'b' or type_contact == "business contact" or type_contact == "business"):
      name = input("Enter name: ")
      num = input("Enter number: ")
      email = input("Enter email: ")
      company = input("Enter company name: ")
      contact = BusinessContact(name, num, email, company)
      self.addContact(contact)
      


list1 = ContactList()
list1.addNewContact()
list1.addNewContact()

list1.display()