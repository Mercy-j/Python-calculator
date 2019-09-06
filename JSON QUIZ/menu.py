import json, sys




def menu():
    while True:
        print("")
        print("1. Bible Quiz."); 
        print("2. Government.");
        print("3. Geography. ");
        print("4. Quit.")
    

        selection = (input("select and play: "))
        

        if selection == "1":
            print("\n BIBLE_QUIZ \n Choose the correct answer from the given option a - d ")
            Bible_Quiz()
        
        elif selection == "2":
            print("\n GOVERNMENT \n Choose the correct answer from the given option a - d ")
            Government()
        
        elif selection == "3":
            print("\n GEOGRAPHY \n Choose the correct answer from the given option a - d ")
            Geography()

        elif selection == "4":
            print("goodbye")
            sys.exit()

        else:
            print("----Invalid choice! Enter 1-4.----")


              
def Bible_Quiz():    
    with open("Quizz.json") as f:
        data = json.load(f)
        exam = data["Bible_Quiz"]
        score = 0

        for i in exam:
            print("")
            print(i["Question"])
            print("(a) " + i["a"])
            print("(b) " + i["b"])
            print("(c) " + i["c"])
            print("(d) " + i["d"])
            ans = input("Your ans: ")
            if ans == i["Answer"]:
                score = score+1
                print("correct\n")
            else:
                print("incorrect answer is " + i["Answer"])
                print("")
        if score <= 2:
            print(" you got " + str(score)+ " out of " + str(len(exam)) + " questions correct, give more time to study your Bible")
        else:
            print(" you got " + str(score)+ " out of " + str(len(exam)) + " questions correct, keep it up")

def Government():    
    with open("governt.json") as f:
        data = json.load(f)
        exam = data["Government"]
        score = 0

        for i in exam:
            print("")
            print(i["Question"])
            print("(a) " + i["a"])
            print("(b) " + i["b"])
            print("(c) " + i["c"])
            print("(d) " + i["d"])
            ans = input("Your ans: ")
            if ans == i["Answer"]:
                score = score+1
                print("correct\n")
            else:
                print("incorrect answer is " + i["Answer"])
                print("")
        if score <= 2:
            print(" you got " + str(score)+ " out of " + str(len(exam)) + " questions correct, give more time to study your Bible")
        else:
            print(" you got " + str(score)+ " out of " + str(len(exam)) + " questions correct, keep it up")

def Geography():    
    with open("geography.json") as f:
        data = json.load(f)
        exam = data["Geography"]
        score = 0

        for i in exam:
            print("")
            print(i["Question"])
            print("(a) " + i["a"])
            print("(b) " + i["b"])
            print("(c) " + i["c"])
            print("(d) " + i["d"])
            ans = input("Your ans: ")
            if ans == i["Answer"]:
                score = score+1
                print("correct\n")
            else:
                print("incorrect answer is " + i["Answer"])
                print("")
        if score <= 2:
            print(" you got " + str(score)+ " out of " + str(len(exam)) + " questions correct, give more time to study your Bible")
        else:
            print(" you got " + str(score)+ " out of " + str(len(exam)) + " questions correct, keep it up")

menu()
            



            
            
