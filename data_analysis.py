"""
File: data_analysis.py
----------------------
This program read in data on cumulative infections of a disease
in different locations, and computes the number of infections
per day at each location.
"""

import sys

# see other filename options inside the data folder
FILENAME = 'data/disease1.txt'


def load_data(filename):
    """
    The function takes in the name of a datafile (string), which
    contains data on locations and their seven day cumulative number
    of infections.  The function returns a dictionary in which the
    keys are the locations in the data file, and the value associated
    with each key is a list of the (integer) values presenting the
    cumulative number of infections at that location.
    """
    cumulative_cases = {}
    with open(filename, 'r') as file:   # Open file to read
        for line in file:
            print(line) 
            
            # Write your code here for part 1!
    
    return cumulative_cases


def daily_cases(cumulative):
    """
    The function takes in a dictionary of the type produced by the load_data
    function (i.e., keys are locations and values are lists of seven values
    representing cumulative infection numbers).  The function returns a
    dictionary in which the keys are the same locations in the dictionary
    passed in, but the value associated with each key is a list of the
    seven values (integers) presenting the number of new infections each
    day at that location.
    """
    
    # Write your code here for part 2!

    return {}




def run_tests():
    # Test 1: load_data
    expected_data = {'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]}
    actual_data = load_data('data/disease1.txt')
    test1 = (actual_data == expected_data)
    print(f"Test 1 (load_data) passed: {test1}")

    # Test 2: daily_cases (Test 1)
    test2_input = {'Test': [1, 2, 3, 4, 4, 4, 4]}
    expected_output2 = {'Test': [1, 1, 1, 1, 0, 0, 0]}
    actual_output2 = daily_cases(test2_input)
    test2 = (actual_output2 == expected_output2)
    print(f"Test 2 (daily_cases) passed: {test2}")

    # Test 3: daily_cases (Test 2)
    test3_input = { 'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13] }
    expected_output3 = { 'Evermore': [1, 0, 0, 0, 0, 0, 0], 'Vanguard City': [1, 1, 1, 1, 1, 1, 1], 'Excelsior': [1, 0, 1, 1, 2, 3, 5] }
    actual_output3 = daily_cases(test3_input)
    test3 = (actual_output3 == expected_output3)
    print(f"Test 3 (daily_cases) passed: {test3}")

    print("Remember, these are just basic tests! Make sure to try other data files")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        run_tests()  # Run the test function if -t is provided
    else:
        data = load_data(FILENAME)
        print(f"Loaded datafile {FILENAME}:")
        print(data)
        print("Daily infections: ")
        print(daily_cases(data))


if __name__ == '__main__':
    main()
