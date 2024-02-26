"""
Task: 
------------------

1. Add another method in the Course class that prints the head office location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal
"""

class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def head_office_loc(self):
        print("Head Office is located in Cape Town")  # No need for a location argument


class OOPCourse(Course):

    def __init__(self):
        super().__init__() # Call the parent class constructor
        self.description = "OOP Fundementals"
        self.trainer = "Mr Anon A. Mouse"
        self.course_id = "#12345"

    def trainer_details(self):
        print("This course is about", self.description, "and is taught by", self.trainer)

    def show_course_id(self):
        print("The course ID is", self.course_id)


course_1 = OOPCourse()  # Create an object without arguments

# Call the methods
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
course_1.head_office_loc()  # Inherited from Course


