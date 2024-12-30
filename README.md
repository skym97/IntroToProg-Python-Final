# Employee Ratings

A Python-based application for managing and analyzing employee performance ratings. This project allows organizations to track, view, and evaluate employee ratings using an easy-to-use API.

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## About the Project
This project was created as the final assignment for the Python programming course at the University of Washington. The goal of this project is to demonstrate the ability to build a functional Python application and document its API for external use.

Employee Ratings is designed to streamline the performance evaluation process. 
Key objectives include:
- Providing a centralized system for employee performance records.
- Allowing managers to submit and update ratings through an API.
- Enabling data-driven insights into team performance.

## Features
- Add and update employee performance ratings.
- Fetch employee details and rating history via an API.
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
2. Access the API via the following endpoints (see full documentation in the `api_docs/` folder):
   - `GET /api/employees` - List all employees.
   - `POST /api/employees` - Add a new employee.

## API Documentation
Comprehensive API documentation is available [here](./api_docs/overview.md).

## Acknowledgments
This project was developed as part of the Python programming course at the University of Washington. Special thanks to my instructor(s) and classmates for their guidance and feedback throughout the course. Additionally, I utilized ChatGPT to help structure the documentation for this project.

## License
Distributed under the MIT License. See `LICENSE` for more information.
