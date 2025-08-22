import random

player = 0
computer = 0

print("===================\nRock Paper Scissors\n===================")

while player != 4:
    player = int(input("Please make your choice, and type a number accordingly:\n1 - ' ✊ ' (Rock)\n2 - ' ✋ ' (Paper)\n3 - ' ✌️  ' (Scissors)\nIf you wish to stop playing, type 4!"))
    computer = random.randint(1, 3)

    if player == 1:
        print("You chose: ✊")
    elif player == 2:
        print("You chose: ✋")
    elif player == 3:
        print("You chose: ✌️")
    elif player == 4:
        break
    else:
        print("Invalid input.")

    if computer == 1:
        print("CPU chose: ✊")
    elif computer == 2:
        print("CPU chose: ✋")
    elif computer == 3:
        print("CPU chose: ✌️")


    if player == 1 and computer == 1:
        print("It's a tie!")
    elif player == 2 and computer == 2:
        print("It's a tie!")
    elif player == 3 and computer == 3:
        print("It's a tie!")
    elif player == 1 and computer == 3:
        print("You win!")
    elif player == 2 and computer == 1:
        print("You win!")
    elif player == 3 and computer == 2:
        print("You win!")
    elif player == 3 and computer == 1:
        print("CPU wins!")
    elif player == 1 and computer == 2:
        print("CPU wins!")
    elif player == 2 and computer == 3:
        print("CPU wins!")
    else:
        print("Invalid result.")

print("Thank you for playing!")