# ------------------------------------------------------------------------------------------------- #
# Title: Processing Classes
# # Description: A collection of the test cases that test the data classes in data_classes.py
# ChangeLog: (Who, When, What)
# BChristopherson, 06-08-2025, Created new script file
# BChristopherson, 06-14-2025, Updated script file
# ------------------------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):

    def test_person_init(self): # Tests the constructor
        person = Person("John", "Johnson")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Johnson")

    def test_person_invalid_name(self): # Tests the first and last name validation
        with self.assertRaises(ValueError):
            person = Person("123", "Johnson")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self): # Tests the __str__() magic method
        person = Person("John", "Johnson")
        self.assertEqual(str(person), "John,Johnson")


class TestEmployee(unittest.TestCase):

    def test_employee_init(self): # Tests the constructor
        employee = Employee("John", "Johnson", "2025-06-13", 5)

        self.assertEqual(employee.first_name, "John")
        self.assertEqual(employee.last_name, "Johnson")
        self.assertEqual(employee.review_date, "2025-06-13")
        self.assertEqual(employee.review_rating, 5)

    def test_employee_review_date(self): # Tests the review_date validation
        with self.assertRaises(ValueError):
            employee = Employee("John", "Johnson", "06-13-2025")

    def test_employee_review_rating(self): # Tests the review_rating validation
        with self.assertRaises(ValueError):
            employee = Employee("John", "Johnson", "06-13-2025", 10)


if __name__ == '__main__':
    unittest.main()
