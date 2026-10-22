
import random

choices = {
    "r": "Stone",
    "p": "Paper",
    "s": "Scissor"
}

computer = random.choice(list(choices.keys()))

youstr = input(
    "Enter your choice (r = Stone, p = Paper, s = Scissor): "
).lower().strip()

if youstr not in choices:
    print("Invalid choice! Please enter r, p, or s.")
else:
    print(f"You chose {choices[youstr]}")
    print(f"Computer chose {choices[computer]}")

    if youstr == computer:
        print("Match is a draw!")
    elif (
        (youstr == "r" and computer == "s")
        or (youstr == "p" and computer == "r")
        or (youstr == "s" and computer == "p")
    ):
        print("You won!")
    else:
        print("You lost!")
