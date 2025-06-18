# ------------------------------------------------------------------------------------------------- #
# Title: Processing Classes
# # Description: A collection of the test cases that test the file processing classes in processing.py
# ChangeLog: (Who, When, What)
# BChristopherson, 06-08-2025, Created new script file
# ------------------------------------------------------------------------------------------------- #

import unittest
import tempfile
import json
import data_classes as data
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
        # Cleans up and deletes the temp test file
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        # Create some test data and write to file
        sample_data =[
            {"FirstName": "John", "LastName": "Johnson",
             "ReviewDate": "2025-06-13", "ReviewRating": 5}
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_data_from_file method and check if it returns the expected data
        employee_data = FileProcessor.read_employee_data_from_file(self.temp_file_name,
                                                                   self.employee_data,
                                                                   data.Employee)

        # Assert that the employee_data list contains the expected employee objects
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, "John")
        self.assertEqual(self.employee_data[0].last_name, "Johnson")
        self.assertEqual(self.employee_data[0].review_date, "2025-06-13")
        self.assertEqual(self.employee_data[0].review_rating, 5)


    def test_write_data_to_file(self):
        # Create some sample employee objects
        sample_employees = [
            data.Employee("Tom", "Jones", "2025-01-01", 3),
            data.Employee("Bob", "Smith", "2024-12-01", 4),
        ]

        # call the wr0te_data_to_file method to write data to the temporary file
        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_employees)

        # Read the data from the temp file and check if it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_employees))
        self.assertEqual(file_data[0]["FirstName"],"Tom")
        self.assertEqual(file_data[0]["ReviewDate"],"2025-01-01")
        self.assertEqual(file_data[1]["LastName"], "Smith")
        self.assertEqual(file_data[1]["ReviewRating"], 4)

if __name__ == "__main__":
    unittest.main()
