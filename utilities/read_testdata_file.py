import csv
import os


class ReadTestdataFile:
    @staticmethod
    def get_file_path():
        #Method to get test data file path using root directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_dir, "data", "test_data.csv")

    @staticmethod
    def read_testdata_csv(testcase_name):
        file_path = ReadTestdataFile.get_file_path()
        data_list = []  # defining empty data list

        try:
            # Open CSV file and define the columns
            with open(file_path, newline='') as file:
                reader = csv.DictReader(file)
                required_columns = {'Test case', 'Username', 'Password', 'Expected condition'}

                # Verify any of the required column is missing
                if not required_columns.issubset(reader.fieldnames):
                    missing_columns = required_columns - set(reader.fieldnames)
                    raise KeyError(f"Missing the following info in testdata file: {missing_columns}")

                # Reading the test id, test case, username, password, expected condition from excel and store it in data_list
                for row in reader:
                    if row['Test case'] == testcase_name:
                        if any(cell.strip() for cell in row.values()):
                            data_list.append((row['Test case'], row['Username'], row['Password'],
                                              row['Expected condition']))

                # Raise error if the csv is empty
                if not data_list:
                    raise ValueError("No data found in the csv file. The file is empty")

            return data_list

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Test data file not found in path {file_path} and the error is {e}")

        except Exception as e:
            raise Exception(f"Unexpected error reading CSV: {e}")
