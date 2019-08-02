#!/usr/bin/python
"""Coding Test Module"""
import sys
import statistics
def take_average(data):
    """Return the average of data"""
    result = float(sum(data))/len(data)
    return result
def take_sum(data):
    """Return the sum of data"""
    result = sum(data)
    return result
def take_median(data):
    """Return the median of data"""
    result = statistics.median(data)
    return result
#The Pythonic way to implement switch statement is to use the powerful dictionary mappings,
#also known as associative arrays, that provide simple one-to-one key-value mappings.
TOKEN_DICT = {
    "take_average" : take_average,
    "take_sum" : take_sum,
    "take_median" : take_median,
}
def calculate_operation(data, arg2):
    """Return the result of sum|avg|median operations"""
    if arg2 == "avg":
        result = TOKEN_DICT["take_average"](data)
        print("The average is ", result)
    elif arg2 == "sum":
        result = TOKEN_DICT["take_sum"](data)
        print("The sum is", result)
    elif arg2 == "median":
        result = TOKEN_DICT["take_median"](data)
        print("The median is ", result)
    else:
        print("enter sum|avg|median")
    return result
def calculate_optional_operation(result, arg3, arg4):
    """Return the result of optional [<gt|lt|eq> <n>] operations"""
    check_number = int(arg4) #get the number to check from command line
    if arg3 == "gt":
        if result < check_number:
            print("input number is greater than result")
        else:
            print("input number is not greater than result")
    elif arg3 == "lt":
        if result > int(check_number):
            print("input number is smaller than result")
        else:
            print("input number is not smaller than result")
    elif arg3 == "eq":
        if result == int(check_number):
            print("input number is equal to the result")
        else:
            print("input number is not equal to result")
def main():
    """Main Function to evaluate data handling functions"""
    if len(sys.argv) > 1:
        filename = sys.argv[1] #get filename from commandline
        with open(filename, 'r') as file:
            data = [float(line.rstrip()) for line in file.readlines()] #read all the data from file
            file.close()# close file
            if not data:
                print("No Data in the file")
            else:
                if len(sys.argv) > 2:
                    arg2 = sys.argv[2]
                    result = calculate_operation(data, arg2)
                    if len(sys.argv) > 3:
                        arg3 = sys.argv[3]
                        arg4 = sys.argv[4]
                        calculate_optional_operation(result, arg3, arg4)
                    else:
                        print("enter [<gt|lt|eq> <n>] as optional arguments")
                else:
                    print("enter sum|avg|median")
    else:
        print("No File with data")
if __name__ == '__main__':
    main()
    