def menu():
   print("1. CreateDB.");
   print("2. Add a record.");
   print("3. Remove the record. ");
   print("4. Searh by a field.");
   print("5. Print all of the records.");
   print("6. Exit.")
   while True:
      try:
          selection= int(input("Select the number you want: "))
          if selection == 1:
             createDB()
             break
          elif selection == 2:
             AddRecord()
             break
          elif selection == 3:
             RemoveRecord()
             break
          elif selection == 4:
             search()
             break
          elif selection == 5:
             printAll()
             break
          elif selection == 6:
             Exit()
             break
          else:
              print("----Invalid choice! Enter 1-6.----")
              
      except ValueError:
           print("Invalid choice! Enter 1-6.")
   exit
   
menu()
dic = {
    "name":input(),
    "surname":input(),
    "age":int(input()),
    "group":input(),
    "addres":input(),
    "email":input(),
}

def createDB():
   global dic
   print("name:", dic["name"])
   print("surname:", dic["surname"])
   print("age:", dic["age"])
   print("group:", dic["group"])
   print("addres:", dic["addres"])
   print("email:", dic["email"])
   print(dic)
   menu() 
It is saying i didnt define function createDB, What did I do wrong?
 


print("""BIBLE QUIZ
\nIts time to test you on the how much you know about God's Word""")
name = input("\nEnter your name: ")
option = input("\nDo you want to play? ")
if option.lower() == "yes" or option.lower() == "y":
