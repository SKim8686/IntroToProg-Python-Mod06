# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   SKim,11/21/23,Functions and Classes Added
# ------------------------------------------------------------------------------------------ #
import json


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

class FileProcessor:
    """
    A class containing processing layer functions that work with JSON files.
    ChangeLog: (Who, When, What)
    SKim,11.21.23,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str) -> list:
        """
        Reads data from a JSON file and returns a list.
        """
        try:
            with open(file_name, "r") as file:
                return json.load(file)
        except Exception as e:
            print("Error: There was a problem with reading the file.")
            print("Please check that the file exists and that it is in a JSON format.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
            return []

    @staticmethod
    def write_data_to_file(file_name: str, data: list) -> None:
        """
        Writes data to a JSON file.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(data, file)
            print("Data has been successfully saved to the file.")
        except Exception as e:
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())


class IO:
    """
    A class containing presentation layer functions that manage user input and output.
    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    SKim,11.21.23,Added menu output and input functions
    SKim,11.21.23,Added a function to display the data
    SKim,11.21.23,Added a function to display custom error messages
    """

    @staticmethod
    def display_menu() -> str:
        """
        Displays the menu and returns the user's choice.
        """
        print(MENU)
        return input("What would you like to do: ")

    @staticmethod
    def get_student_input() -> dict:
        """
        Takes user input for student information and returns a dictionary.
        """
        try:
            first_name = input("Enter the student's first name: ")
            if not first_name.isalpha():
                raise ValueError("The first name should only contain alphabetic characters.")
            last_name = input("Enter the student's last name: ")
            if not last_name.isalpha():
                raise ValueError("The last name should only contain alphabetic characters.")
            course_name = input("Please enter the name of the course: ")
            return {"FirstName": first_name, "LastName": last_name, "CourseName": course_name}
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
            return {}

    @staticmethod
    def display_students(students: list) -> None:
        """
        Displays the student information.
        """
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def display_error_message(message: str) -> None:
        """
        Displays a custom error message.
        """
        print("Error:", message)

# Define the Data Variables and constants
FILE_NAME = "students.json"
student_data = FileProcessor.read_data_from_file(FILE_NAME)

# Present and Process the data
while True:
    menu_choice = IO.display_menu()

    # Input user data
    if menu_choice == "1":
        student_input = IO.get_student_input()
        if student_input:
            student_data.append(student_input)
            print(f"You have registered {student_input['FirstName']} {student_input['LastName']} for {student_input['CourseName']}.")

    # Present the current data
    elif menu_choice == "2":
        IO.display_students(student_data)

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, student_data)

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
