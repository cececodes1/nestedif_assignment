# Remember to take your time and work through each question diligently! 
# Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, 
# then turn in your Github link at the bottom of the page!

# Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

# Nested Decisions: The Adventure Game 🏰
# Objective: To practice the use of nested if statements.

# Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. 
# Identify and fix them.

#Buggy Code:

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        action == "cross a river"
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")



# Task 2: Setting the Scene

# Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch"
# or "proceed in the dark", and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a sloth!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    choice = input("light a torch or proceed in the dark? ")
    if choice == "light a torch":
        print("You find a hidden treasure!")
    elif choice == "proceed in the dark":
        print("You came across a secret passageway!")


#Task 3: Default Path

#If the user makes an invalid choice at any point, incorporate a pass statement to handle it.
# HINT: How can an else statement be of use here?
        
    elif place == "cave":
        choice = input("light a torch or proceed in the dark? ")
    if choice == "light a torch":
        print("You find a hidden treasure!")
    elif choice == "proceed in the dark":
        print("You stumble upon a secret passage!")
    else:
        print("Invalid choice. Please choose 'light a torch' or 'proceed in the dark'.")
        
else:
    print()
    pass