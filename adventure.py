import time

def display_intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself standing in front of a dark cave.")
    print("Legend has it that a great treasure is hidden inside.")
    print("But beware, many adventurers have entered the cave and never returned...")

def choose_path():
    path = input("Do you enter the cave? (y/n)").lower()
    if path == "y":
        print("You enter the cave...")
        time.sleep(2)
        print("You see two paths ahead of you...")
        time.sleep(2)
        print("One path leads to the left, and the other to the right.")
        time.sleep(2)
        return True
    else:
        print("You decide not to enter the cave.")
        return False

def choose_direction():
    direction = input("Do you go left or right? (l/r)").lower()
    if direction == "l":
        print("You head left...")
        time.sleep(2)
        print("You come across a giant spider!")
        time.sleep(2)
        print("You defeat the spider and continue on...")
        time.sleep(2)
        return True
    elif direction == "r":
        print("You head right...")
        time.sleep(2)
        print("You come across a bottomless pit!")
        time.sleep(2)
        print("You try to jump over it, but you fall in and die...")
        time.sleep(2)
        return False
    else:
        print("Invalid input. Please enter 'l' or 'r'.")
        return choose_direction()

def main():
    display_intro()
    if choose_path():
        if choose_direction():
            print("Congratulations, you found the treasure!")
        else:
            print("Game over.")
    else:
        print("Game over.")

if __name__ == '__main__':
    main()
