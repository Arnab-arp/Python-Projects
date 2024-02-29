#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final_grades = []
    print(grades.pop(0))
    for grade in grades:
        next_multiple = grade  # initial grade
        for _ in range(1, 4):
            next_multiple += 1
            if next_multiple % 5 == 0:
                break
        grade_determiner = next_multiple - grade

        if next_multiple < 40:
            final_grades.append(grade)
        else:
            if grade_determiner < 3:
                final_grades.append(next_multiple)
            elif grade_determiner == 3:
                final_grades.append(grade)
    return final_grades


if __name__ == '__main__':
    hanabi = [4, 73, 67, 38, 33]
    print(gradingStudents(hanabi))