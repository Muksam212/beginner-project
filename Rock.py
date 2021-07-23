import random

user_wins=0
computer_wins=0

options=['rock','paper','scissors','test']
while True:
    user_input=input("Type Rock/Paper/Scissors or Q to quit:").lower()
    if user_input=="q":
        quit()

    if user_input not in options:
        continue

    random_number=random.randint(1,2)
    #rock is 0, paper is 1 and scissors is 2

    computer_pick=options[random_number]
    print("Computer picked:", computer_pick+ " . ")

    if user_input=="rock" and computer_pick=="scissors":
        print("You won!")
        user_wins+=1
        continue
    if user_input=="paper" and computer_pick=="rock":
        print("You won!")
        user_wins+=1
        continue


print("Goodbye!")