print("Welcome to quiz game!")

player=input("Do you want to play? ")

if player.lower()!= 'yes':
    quit()

print("Okay let's play:)")
score=0

answer=input("What does CPU stands for? ").lower()
if answer=="central processing unit":
    print("Correct!")
    score+=1

else:
    print("Incorrect")

answer=input("What does CSV stands for? ").lower()
if answer=="comma seperate value":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer=input("What does LR stands for? ").lower()
if answer=="linear regression":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print("You got:"+str(score)+ "Question Correctly")
print("You got:"+str(score/3)*100+ "Question correctly")