"""
This file contains intentional code quality issues to test static code analyzers.
"""
import time
import os
import json
import random
import math
import sys
import re


# Global variables - bad practice
global_data = []
PASSWORD = "hardcoded_password"  # Sensitive data in code


def unused_parameter_function(param1, param2):
    """This function declares parameters it doesn't use"""
    return "Only using param1: " + param1


class PoorlyDesignedClass:
    """Class with multiple code quality issues"""
    
    def __init__(self):
        # Too many instance attributes - code smell
        self.attr1 = 1
        self.attr2 = 2
        self.attr3 = 3
        self.attr4 = 4
        self.attr5 = 5
        self.attr6 = 6
        self.attr7 = 7
        self.attr8 = 8
        self.attribute9 = 9
        self.attribute10 = 10
        
    def duplicate_code_1(self, items):
        """Function with duplicate code pattern"""
        result = []
        for item in items:
            value = item * 2 + 10
            if value > 30:
                result.append(value)
        return result
    
    def duplicate_code_2(self, items):
        """Almost identical to the previous function"""
        output = []
        for item in items:
            value = item * 2 + 10
            if value > 30:
                output.append(value)
        return output
    
    def complex_function(self, a, b, c, d, e, f):
        """Function with high cyclomatic complexity"""
        result = 0
        
        if a > 0:
            if b > 0:
                if c > 0:
                    result = a + b + c
                else:
                    if d > 0:
                        result = a + b + d
                    else:
                        result = a + b
            else:
                if e > 0:
                    if f > 0:
                        result = a + e + f
                    else:
                        result = a + e
                else:
                    result = a
        else:
            if b > 0:
                result = b
            else:
                if c > 0:
                    result = c
                else:
                    if d > 0:
                        result = d
                    else:
                        if e > 0:
                            result = e
                        else:
                            result = f
        
        return result


def long_function():
    """A very long function that should be refactored"""
    # Overly long function with too many lines
    results = []
    for i in range(100):
        if i % 2 == 0:
            results.append(i * 2)
        else:
            results.append(i * 3)
    
    for i in range(100):
        if i % 3 == 0:
            results.append(i * 4)
        else:
            results.append(i * 5)
    
    for i in range(100):
        if i % 4 == 0:
            results.append(i * 6)
        else:
            results.append(i * 7)
            
    # More repetitive code...
    processed = []
    for result in results:
        processed.append(result + 10)
        
    processed_again = []
    for item in processed:
        processed_again.append(item * 2)
        
    return sum(processed_again)


def poorly_named_func(x):
    """Function with ambiguous variable names"""
    a = x + 10
    b = a * 2
    c = b - 5
    return c


def risky_file_handling(filename):
    """Does not properly close file handles"""
    f = open(filename, 'r')  # Not using 'with' statement
    data = f.read()
    # No f.close() - resource leak


def broad_exception_handling():
    """Catches all exceptions and passes silently"""
    try:
        x = 10 / 0
        return x
    except:  # Bare except clause - catches all exceptions including KeyboardInterrupt
        pass  # Silent failure


def parse_json_risky(json_string):
    """Function with error-prone type handling"""
    data = json.loads(json_string)
    # Using dynamic attribute access without type checking
    return data['name'] + " is " + str(data['age']) + " years old and has score: " + str(data['score'])


# Dead code that is never called
def dead_function():
    """This function is never called from anywhere"""
    print("This is dead code")
    return None


# Inconsistent return statements
def inconsistent_returns(value):
    """Function with inconsistent return types"""
    if value > 10:
        return "Greater than 10"
    elif value < 0:
        return -1  # Returning integer instead of string
    else:
        return None  # Returning None instead of string


if __name__ == "__main__":
    # Too many temporary variables
    temp1 = 10
    temp2 = 20
    temp3 = temp1 + temp2
    temp4 = temp3 * 2
    temp5 = temp4 - 15
    temp6 = str(temp5)
    temp7 = "Result: " + temp6
    print(temp7)