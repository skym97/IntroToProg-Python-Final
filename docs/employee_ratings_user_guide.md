# User Guide for Employee Ratings

This guide provides step-by-step instructions for using the Employee Ratings application, which is designed to manage and analyze employee performance data.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Setup](#setup)
- [Using the Application](#using-the-application)
  - [Starting the Application](#starting-the-application)
  - [Menu Options](#menu-options)

## Overview
The Employee Ratings application is a Python-based program for managing employee performance reviews. It allows user to view, update, and save employee data efficiently.

## Requirements
- Python 3.8 or higher
- A JSON file named `EmployeeRatings.JSON` in the root directory

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/employee-ratings.git
   ```

2. Navigate to the project directory:
  ```bash
   cd employee-ratings
   ```

3. Ensure the `EmployeeRatings.JSON` file exists and is formatted correectly. If not, create one with the following structure:
 ```bash
   [
     {
       "FirstName": "John",
       "LastName": "Doe",
       "ReviewDate": "2023-01-01",
       "ReviewRating": 4
    }
  ]
   ```

4. Run the Application:
  ```bash
   python src/main.py
   ```

## Using the Application

### Starting the Application
1. Open a terminal or Command Prompt

2. Navigate to the src folder:
  ```bash
   cd src
   ```

3. Run the program:
  ```bash
   python main.py
   ```

## Menu Options
After starting the application, you will see the following menu:
```bash
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
  ```

### Option 1: Show Current Employee Rating Data
- Displays all employee data currently stored in memory, including:
  - Full Name
  - Review Date
  - Review Rating

### Option 2: Enter New Employee Rating Data
- Prompts you to enter:
  - First Name
  - Last Name
  - Review Date (YYYY-MM-DD format)
  - Review Rating (1 - 5 scale)
- Adds the new employee data to memory.

### Option 3: Save Data to a File
- Saves all current employee data in memory to `EmployeeRatings.JSON`
- Confirms success with a message.

### Option 4: Exit the Program
- Ends the Program
- Any unsaved changes will be lost
