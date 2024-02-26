""" 
Basic OOP Email Simulator
"""

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

    # Declare the class variable, with default value, for emails. 
 
    # Initialise the instance variables for emails.

    # Create the method to change 'has_been_read' emails from False to True.

class Email:
    # Constructor method
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    # Method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.

inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    email1 = Email("hugob@sample.com", "Test 1", "Hi! I have submitted Test 1")
    email2 = Email("nicoleb@sample.com", "Groceries", "Reminder to get the groceries on the list I gave you.")
    email3 = Email("chrisb@sample.com", "Test 3", "Just wanted to remind you of test 2 tomorrow!")

    # Add emails to the list
    inbox.extend([email1, email2, email3])

    return inbox


def list_emails(emails):  # Add "emails" as a parameter
    for index, email in enumerate(emails, start=1):
        print(f"{index}. {email.subject_line}")

def read_email(index):
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    global selected_email # Declare as global to access in menu input 1
    if 1 <= index <= len(inbox):
        selected_email = inbox[index - 1]
        print(f"\nFrom {selected_email.email_address}\nSubject: {selected_email.subject_line}\n\n{selected_email.email_content}")
        selected_email.mark_as_read()
        print(f"\nEmail '{selected_email.subject_line}' from {selected_email.email_address} marked as read.\n")

    else:
        print("\nWhat if I told you, that that is an invalid email index.")
    


# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while True:
    try:
        user_choice = int(input('''\nGreetings weary traveller!
        Choose your email destination:
        1. Read an email
        2. View unread emails
        3. Quit application

        Enter selection: '''))
        
        if user_choice == 1:
            # add logic here to read an email
            list_emails(inbox)
            while True:
                try:
                    email_index = int(input("\nPlease enter the number of the email you want to view: "))
                    read_email(email_index)
                    break
                except ValueError:
                    print("\nBathong! Invalid input. Please enter a number from the presented options.")

        elif user_choice == 2:
            # add logic here to view unread emails
            # Inside the menu logic for viewing unread emails:
            unread_emails = [email for email in inbox if not email.has_been_read]
            if unread_emails:
                for email in unread_emails:
                    print(f"- {email.subject_line}")
            else:
                print("\nNo unread emails. Go out and socialise!")

                
        elif user_choice == 3:
            # add logic here to quit appplication
            print("\nI don't always exit the application, but for you, I will.\n")
            break

        else:
            print("\nThat moment when you realise you entered a number not listed in the presented options.")

    except ValueError:
        print("\nNumbers people, not any other characters. Please enter a number from the presented options.")