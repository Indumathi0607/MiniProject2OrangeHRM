import csv
import os.path
from datetime import datetime

class WriteIntoTestDataFile:
    # Class variable to auto generate serial number and test id
    s_no_generator = 0
    testcase_ID_generator = 0

    @classmethod
    def get_s_no(cls):
        cls.s_no_generator += 1
        return cls.s_no_generator

    @classmethod
    def get_testcase_ID(cls):
        cls.testcase_ID_generator += 1
        return f"GUVI_{cls.testcase_ID_generator:02d}"  # Returns testcase id in GUVI_01 format


    @staticmethod
    def get_file_path(): #Method to find the absolute path of test_data file
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_dir, "data", "test_data.csv")

    @staticmethod
    def write_test_result(testcase_name, username, password, expected_condition, test_result):
        # file path
        file_path = WriteIntoTestDataFile.get_file_path()
        file_exists = os.path.exists(file_path)

        # Defining column headers
        headers = ["S No", "Test ID", "Tester name", "Date", "Test case", "Username", "Password", "Expected condition",
                   "Test result"]

        # Assigning values for each row
        date = f"'{datetime.now().strftime('%Y-%m-%d')}"
        tester = "Indu"

        # Read test data file for existing data
        rows = []
        if file_exists:
            with open(file_path, mode="r", newline="") as file:
                reader = csv.reader(file)
                existing_headers = next(reader, None)  # Reading existing headers
                rows = list(reader)  # Reads all rows

            found = False
            for i, row in enumerate(rows):
                if len(row) >= 7 and row[4] == testcase_name and row[5] == username and row[
                    6] == password:  # Reading the testcase name, username, password of each row
                    rows[i] = [WriteIntoTestDataFile.get_s_no(), WriteIntoTestDataFile.get_testcase_ID(),
                               tester, date, testcase_name, username, password, expected_condition, test_result]

                    found = True
                    break

            if not found:
                # If no data entry found then create new entry
                rows.append([WriteIntoTestDataFile.s_no_generator, WriteIntoTestDataFile.testcase_ID_generator,
                             tester, date, testcase_name, username, password, expected_condition, test_result])

        # Write all data back to file
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write headers
            writer.writerow(headers)
            # Write all rows
            writer.writerows(rows)
