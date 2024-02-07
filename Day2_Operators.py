#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    mtip = (meal_cost * (tip_percent / 100))
    mtax = (meal_cost * (tax_percent/ 100))
    total = int(round(meal_cost + mtip + mtax))
    
    print(total)

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)


# -------- How Someone else Solved ----- #
def get_total_cost_of_meal():
    # original meal price
    meal_cost = float(input())
    # tip percentage
    tip_percent = int(input())
    # tax percentage
    tax_percent = int(input())

    # Write your calculation code here
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100

    # cast the result of the rounding operation to an int and save it as total_cost 
    total_cost = int(round(meal_cost + tax + tip))
    
    return str(total_cost)

# Print your result
print("The total meal cost is " + get_total_cost_of_meal() + " dollars.")
