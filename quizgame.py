print("Welcome to the Quiz Game")

playing = input("Do you want to play? ")

if playing.lower != "yes":
    quit()

print("Okay let's play! ")

answer = input("What does CPU stand for? ")
if answer.lower == "central processing unit":
    print("Correct!")
else:
    print("incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower == "graphics processing unit":
    print("Correct!")
else:
    print("incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower == "ranson access memory":
    print("Correct!")
else:
    print("incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower == "power supply":
    print("Correct!")
else:
    print("incorrect!")