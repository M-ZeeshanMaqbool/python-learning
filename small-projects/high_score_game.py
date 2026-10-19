
import random


def game():
    print("You are playing...")

    score = random.randint(1, 70)

    with open("myfile.txt", "a+") as f:
        f.seek(0)
        data = f.read().strip()
        hiscore = int(data) if data else 0

    print(f"Your score is: {score}")
    print(f"Previous high score is: {hiscore}")

    if score > hiscore:
        with open("myfile.txt", "w") as f:
            f.write(str(score))
        print("Congratulations! New high score!")

    return score


game()
