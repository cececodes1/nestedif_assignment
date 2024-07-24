#Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

#Buggy Code:

# convert the input to an integer before comparing to 100
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" 
# based on the number of attendees.

attendees = int(input("Enter number of attendees: "))
venu = "large hall" if attendees > 100 else "conference room"

# recommended audio system and projector if the venue is the large hall
if venu == "large hall":
    print("You may need an audio system.")
    print("You may need a projector also.")
elif venu == "conference room":
    print("nothing else needed")


# Task 3: Catering Choices: Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" 
# if yes, otherwise recommend "Gourmet Meals Caterers".
    
    choice = input("Do you want vegetarian food? (yes/no): ")
if choice == "yes":
    print("We recommend 'Veggie Delight Caterers' for your event!")
else:
    print("We recommend 'Gourmet Meals Caterers' for your event!")