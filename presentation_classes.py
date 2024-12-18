
# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Andy Sul, 11/30/24, Modified Script
# ------------------------------------------------------------------------------------------------- #

from data_classes import Employee  # Import the Employee class
import json
from datetime import date

class IO:
    """
    A collection of presentation layer functions that manage user input and output
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        :return: None
        """
        print()
        print(menu)
        print()


    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice


    @staticmethod
    def output_employee_data(employee_data: list):
        """ This function displays employee data to the user

        :param employee_data: list of employee object data to be displayed

        :return: None
        """
        print()
        print("-" * 50)
        for employee in employee_data:
            # Add the review rating description based on the employee's review_rating
            if employee.review_rating == 5:
                message = " {} {} is rated as 5 (Leading), Review Date: {}, Rating: {}"
            elif employee.review_rating == 4:
                message = " {} {} is rated as 4 (Strong), Review Date: {}, Rating: {}"
            elif employee.review_rating == 3:
                message = " {} {} is rated as 3 (Solid), Review Date: {}, Rating: {}"
            elif employee.review_rating == 2:
                message = " {} {} is rated as 2 (Building), Review Date: {}, Rating: {}"
            elif employee.review_rating == 1:
                message = " {} {} is rated as 1 (Not Meeting Expectations), Review Date: {}, Rating: {}"

            # Print the formatted string
            print(message.format(employee.first_name, employee.last_name, employee.review_date, employee.review_rating))
        print("-" * 50)
        print()

    @staticmethod
    def input_employee_data(employee_data: list, employee_type: Employee):
        """ This function gets the first name, last name, and GPA from the user

        :param employee_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            # Input the data
            employee_object = employee_type()
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date? ")
            employee_object.review_rating = int(input("What is their review rating? "))
            employee_data.append(employee_object)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data
