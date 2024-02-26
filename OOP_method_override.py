"""
OOP method override demonstration
"""
# Store user data.
# Allows to call user() multiple times to get user input in different parts of code for different reasons.
def user():
    user_info = {}
    user_info["name"] = input("Please enter your name: ")

    # Error checking for invalid age inputs
    while True:
        try:
            user_info["age"] = int(input("Please enter your age: "))
            if user_info["age"] <= 0: 
                raise ValueError("Age cannot be zero or negative.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")

    user_info["eye_colour"] = input("Please enter your eye colour: ")
    user_info["hair_colour"] = input("Please enter your hair colour: ")
    return user_info

class Adult:

    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self): 
        # Logic can also be inserted here to auto determine driver eligibility
        # However, the current method allows for later customisation of Child driver status, ie Learners Licence
        print(f"{self.name} is an adult and is old enough to drive.")

class Child(Adult):
        
    def can_drive(self):    
        print(f"{self.name} is too young and is not old enough to drive.")

user_data = user()  # Store user information
if user_data["age"] >= 18:
    person = Adult(**user_data)   # Unpack user_data into arguments for Adult due to being saved as dictionary
else:
    person = Child(**user_data)  # Unpack user_data into arguments for Child

person.can_drive()  # Check driving eligibility