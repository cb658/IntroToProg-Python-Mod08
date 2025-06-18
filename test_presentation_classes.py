# ------------------------------------------------------------------------------------------------- #
# Title: Processing Classes
# # Description: A collection of the test cases that test the inpout & output classes in presentation.py
# ChangeLog: (Who, When, What)
# BChristopherson, 06-08-2025, Created new script file
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch

from data_classes import Employee
from presentation_classes import IO

class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data = []

    def test_input_menu_choice(self):
        # Simulate user input '2' and check if the function returns '2'
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self):
        # Simulate user input for employee data
        with patch('builtins.input', side_effect=['John', 'Johnson', '2025-06-13', 5]):
            IO.input_employee_data(employee_data=self.employee_data, employee_type=Employee)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'John')
            self.assertEqual(self.employee_data[0].last_name, 'Johnson')
            self.assertEqual(self.employee_data[0].review_date, "2025-06-13")
            self.assertEqual(self.employee_data[0].review_rating, 5)

    # //TODO update the code below to be review date and review rating
        # Simulate invalid GPA input (not a float)
        with patch('builtins.input', side_effect=['Alice', 'Smith', 'invalid', 10]):
            IO.input_employee_data(employee_data=self.employee_data, employee_type=Employee)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

if __name__ == "__main__":
    unittest.main()