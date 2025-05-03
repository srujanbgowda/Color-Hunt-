import random

def get_clue(target, guess):
    clues = []
    for i, color in enumerate(["Red", "Green", "Blue"]):
        if guess[i] < target[i]:
            clues.append(f"{color} is too low")
        elif guess[i] > target[i]:
            clues.append(f"{color} is too high")
        else:
            clues.append(f"{color} is correct")
    return clues

print("=== Color Hunt Challenge ===")
target_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
attempts = 0

while True:
    try:
        r = int(input("Guess Red (0-255): "))
        g = int(input("Guess Green (0-255): "))
        b = int(input("Guess Blue (0-255): "))
        guess = (r, g, b)
        attempts += 1

        if guess == target_color:
            print(f"Correct! You found the color in {attempts} tries!")
            print(f"RGB was: {target_color}")
            break
        else:
            clues = get_clue(target_color, guess)
            print("Clues:")
            for clue in clues:
                print("-", clue)
            print()
    except:
        print("Please enter valid numbers (0-255).")