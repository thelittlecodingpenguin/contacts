from replit import db
from os import system
import time
import stdiomask


def clear():
  system("clear")


def init():
  global user
  global contacts
  global password
  option = input("Which of the following do you want to do? (signup/login)\n> ").lower().strip()
  if option == "login":
    user = input("What is your username?\n> ")
    password = stdiomask.getpass("What is your password?\n> ")
    try:
      contacts = db[user, password]
    except KeyError:
      print("Not found")
      clear()
      init()
  elif option == "signup":
    user = input("What is your username?\n> ")
    if user in db:
      print("Already taken username")
      clear()
      init()
    else:
      print("Your password has to be more than 8 characters")
      password = stdiomask.getpass("What is your password?\n> ")
      if len(password) <= 8:
        print("Password is too short")
        time.sleep(4)
        clear()
        init()
      contacts = {}
  else:
    print("Invalid choice")
    time.sleep(4)
    clear()
    init()


def sync():
  db[user, password] = contacts


def delete():
  name = input("What do you want to delete?\n> ")
  if len(contacts) == 0:
    print("You have no contacts yet")
    time.sleep(4)
    clear()
    init()
  else:
    contacts.pop(name)
    sync()


def information():
  name = input("What is the name?\n> ")
  if name in contacts:
    print("Name already taken")
    time.sleep(4)
    clear()
    init()
  else:
    phone = input("What is the phone number?\n> ")
    contacts[name] = phone
    sync()


def search():
  search = input("What name are you looking for?\n> ")
  try:
    if contacts[search]:
      print("Phone number:", contacts[search])
  except:
    print("Not found")
    time.sleep(4)
    init()
    clear()


def check(option):
  if option == "add a name":
    information()
  elif option == "look up a name":
    if len(contacts) == 0:
      print("You have no contacts yet")
      time.sleep(4)
      clear()
      init()
    else:
      search()
  elif option == "delete a name":
    delete()
  sync()


def MainLoop():
  while True:
    message = "WELLCOME TO PHONEBOOK"
    print(message)
    time.sleep(4)
    clear()
    option = input("Which of the following do you want to do? (Add a name/look up a name/delete a name)\n> ").lower().strip()
    check(option)
        

def main():
  init()
  MainLoop()


if __name__ == "__main__":
  main()

