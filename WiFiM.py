import os
import time
import random
def out_red(text):
    print("\033[31m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))
def out_green(text):
    print("\033[32m {}" .format(text))
password = "Harington18901"
login = "AdminM"
login1 = input("Enter your Login here : ")
if login1 in login:
  sleep(1)
  password1 = input("Enter your Password here : ")
  if password1 in password:
    sleep(1.6)
    os.system("clear")
    sleep(0.8)
    out_red("MY - WiFiM")
    sleep(0.4)
    out_red("by HopStop | Myha")
    sleep(0.6)
    out_green("1 - WiFi Vulnerabion")
    menu = input("Select an item from the menu : ")
    if menu == "1":
      sleep(0.4)
      os.system("clear")
      sleep(0.2)
      choice = "Y"
      
      while choice.lower() == "Y":
        sleep(0.3)
        start = input("Press Y to start the attack or any other key to end the program : ")
        time.sleep(0.3)
        out = input("IP WiFi? : ")
        time.sleep(2)
        out_green("Please, wait...")
        os.system("apt update")
        wifihack1 = "Done! The hacking was successful, the password file is stored in WiFi1.txt."
        wifihack2 = "Mistake! The password was not found."
        wifihack = random.randomint(wifihack1, wifihack2)
        
        out_green(wifihack)
        sleep(27)
      else:
        sleep(0.3)
        print("Completion of the program...")
else:
  sleep(1)
  print("Error!")
