# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# BChristopherson, 06-08-2025, Created new script file
# ------------------------------------------------------------------------------------------------- #

import json
from datetime import date


#// TODO - check if all these are need in main.py
import data_classes as dc
import processing_classes as proc
import presentation_classes as pres


# Beginning of the main body of this script
employees = proc.FileProcessor.read_employee_data_from_file(file_name=dc.FILE_NAME,
                                                       employee_data=dc.employees,
                                                       employee_type=dc.Employee)  # Note this is the class name (ignore the warning)

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=dc.MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = pres.IO.input_employee_data(employee_data=employees, employee_type=Employee)  # Note this is the class name (ignore the warning)
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=dc.FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {dc.FILE_NAME} file.")
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
