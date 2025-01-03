# Employee Ratings

A Python-based application for managing and analyzing employee performance ratings. This project allows organizations to track, view, and evaluate employee ratings using an easy-to-use interface.

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## About the Project
This project was created as the final assignment for the Foundations of Programming (Python) certificate course at the University of Washington. The goal of this project is to demonstrate the ability to build a functional Python application. The documentation created for this is something I created on my own time and not part of the final project. 

Employee Ratings is designed to streamline the performance evaluation process. 
Key objectives include:
- Providing a centralized system for employee performance records.
- Allowing managers to submit and update ratings efficiently.
- Enabling data-driven insights into team performance.

## Features
- Add and update employee performance ratings.
- View a detailed list of employee reviews, including performance descriptions (e.g., "Leading" for a rating of 5).
- Save and load employee data from a JSON file.
- Error handling for invalid input or unauthorized requests.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/employee-ratings.git
   ```
2. Navigate to the project directory:
   ```bash
   cd employee-ratings
   ```
3. Run the application:
   ```bash
   python src/main.py
   ```

## Usage
1. Navigate to the `src/` directory and run the application:
   ```bash
   python main.py
   ```
2. The program provides the following functionality through a text-based menu:
   - Option 1: Display current employee rating data.
   - Option 2: Enter new employee rating data, including first name, last name, review date, and rating (1-5).
   - Option 3: Save data to the `EmployeeRatings.json` file.
   - Option 4: Exit the program.

## File Structure Overview
- `data_classes.py`: Defines the Employee class, which represents individual employee data.
- `presentation_classes.py`: Handles user interactions, such as displaying menus and collecting input.
- `processing_classes.py`: Manages reading from and writing to the EmployeeRatings.json file.
- `main.py`: The entry point of the application, orchestrating functionality across modules.

## Acknowledgments
This project was developed as part of the Python programming course at the University of Washington. Special thanks to my instructor(s) and classmates for their guidance and feedback throughout the course. Additionally, I utilized ChatGPT to provide a guideline for documentation.
