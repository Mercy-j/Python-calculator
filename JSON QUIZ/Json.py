
import json

print("""BIBLE QUIZ
\nIts time to test you on the how much you know about God's Word""")
name = input("\nEnter your name: ")
option = input("\nDo you want to play? ")
print("")
if option.lower() == "yes" or option.lower() == "y":
    with open("Quizz.json") as f:
        data = json.load(f)
        exam = data["Bible_Quiz"]
        score = 0

        for i in exam:
            print(i["Question"])
            print("(a) " + i["a"])
            print("(b) " + i["b"])
            print("(c) " + i["c"])
            print("(d) " + i["d"])
            ans = input("choose the correct answer from the given option a - d: ")
            if ans == i["Answer"]:
                score = score+1
                print("correct\n")
            else:
                print("incorrect answer is " + i["Answer"])
                print("")
        if score <= 2:
                print(name + " you got " + str(score)+ " out of " + str(len(exam)) + " questions correct, give more time to study your Bible")
        else:
                print(name + " you got " + str(score)+ " out of " + str(len(exam)) + " questions correct, keep it up")
            

print("Thank you, Good bye")
exit()

