# Code Documentation for Employee Ratings

## Overview

The Employee Ratings application is designed to manage and analyze employee performance data. This code is modularized into distinct files to separate concerns, making it easier to maintain and extend. Below is detailed documentation of each module, class, and function.

## Modules Overview

1. `main.py`
The main entry point of the application. It integrates various modules and manages the program's control flow.

2. `data_classes.py`
Contains the core data model for the application, including `Person` and `Employee` classes.

3. `presentation_classes.py`
Manages input and output, including user interaction and data display.

4. `processing_classes.py`
Handles data persistence, including reading and writing to the JSON file.

## Class and Function Details

### `main.py`

Global Variables:

- `FILE_NAME`: The default filename for storing employee data (`EmployeeRatings.json`).

- `MENU`: The text displayed for the user menu.

- `employees`: A list to store employee objects.

Main Script Flow:

- Reads employee data from the file using `FileProcessor.read_employee_data_from_file`.

- Loops through the menu options, allowing users to interact with the application.

- Includes menu-driven functionality to view, add, save, or exit.

### `data_classes.py`

#### `class Person`
Represents basic personal information.

Attributes:

- `first_name` (str): The person's first name

- `last_name` (str): The person's last name

Methods:

- `__str__()`: Returns a formatted string representation of the object.

#### `class Employee`
Extends `Person` to include employee-specific attributes.

Attributes:

- `review_date` (str): The date of the employee review (YYYY-MM-DD).

- `review_rating` (int): The review rating (1-5).

Methods:

- `__str__()`: Returns a formatted string representation, including review details.

### `presentation_classes.py`

`class IO`
Manages user input and output.

Key Methods:

- `output_error_messages(message, error)`: Displays error messages.

- `output_menu(menu)`: Prints the menu options.

- `input_menu_choice()`: Prompts user for a menu choice and validates it.

- `output_employee_data(employee_data)`: Displays employee details in a user-friendly format.

- `input_employee_data(employee_data, employee_type)`: Collects new employee information from the user.

### `processing_classes.py`

`class FileProcessor`
Handles file operations.

Key Methods:

- `read_employee_data_from_file(file_name, employee_data, employee_type)`: Reads data from a JSON file and populates the employee list.

- `write_employee_data_to_file(file_name, employee_data)`: Writes the employee list to a JSON file.

## Dependencies

- `json`: For reading and writing JSON data.

- `datetime.date`: For validating date inputs.

- Custom Imports

  - `Employee` from `data_classes`
 
  - Functions from `presentation_classes` and `processing_classes`
 
## Notes

- Ensure the `EmployeeRatings.JSON` file exists before running the program.

- The code includes robust error handling for user inputs and file operations.
