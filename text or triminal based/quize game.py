print("Welcome to my Quize Game.")

name = input("Please Enter your Name\n").title()

print(f"Hello {name}, Welcome.")

playing = input("Are you ready to play? ").lower()

if playing != "yes":
    print("See you when you are Ready.")
    quit()

print("Let's go!!")

print("The Rules are you only get one try for each question.")

score = 0

print("True Or False")

answer = input("Whales are mammals, not fish.\n").lower()

if answer != "true":
    print("You are Worng")
else:
    print("You are Correct")
    score += 1

answer = input("Sharks are mammals.\n").lower()

if answer != "true":
    print("You are Worng")
else:
    print("You are Correct")
    score += 1
    
    
answer = input("Bees can see all colors except red.\n").lower()

if answer != "true":
    print("You are Worng")
else:
    print("You are Correct")
    score += 1


answer = input("The human heart has four chambers.\n").lower()

if answer != "true":
    print("You are Worng")
else:
    print("You are Correct")
    score += 1
    
print(f"Your score is {score}")  
print(f"Your score in percentage is {(score/4) * 100}")