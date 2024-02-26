"""
A basic quiz demonstrating key skills
"""

print("\nWelcome to the quiz!\n")

playing = input("Do you want to start the quiz? (y/n) ")

score = 0

if playing.lower() != "y":
    print("Goodbye!")
    quit()

print("Okay! Let's go!")

answer= input("What does API stand for? ")
if answer.lower()  == "application programming interface":
    print("Correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

answer = input("What does LAN stand for? ")
if answer.lower()  == "local area network":
    print("Correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

answer = input("What does IP stand for? ")
if answer.lower()  == "internet protocol":
    print("Correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

answer = input("What does DNS stand for? ")
if answer.lower()  == "domain name system":
    print("Correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%!")
