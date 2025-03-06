#!/usr/bin/env python3
"""
tipCalculator.py - A simple tip calculator.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/06
License: MIT
Dependencies: None (built-in functions only)

Description:
This script calculates the total amount to be paid per person, including the tip.
It takes the following user inputs:
1. The total bill amount.
2. The percentage of the tip.
3. The number of people splitting the bill.

The script then calculates the total amount per person and displays the result.

Usage:
Run the script and follow the prompts:
    python tipCalculator.py

Example Output:
    Enter the total bill: 100
    Enter the tip percentage: 15
    Enter the number of people: 4
    Each person should pay: $28.75
"""

#User inputs, amount oif the entire bill, the tip percentage and the amount of people splitting the bill
bill = float(input("What's the total bill amount: "))
tip = float(input("What's the percentage of the tip you want to leave: "))
people = float(input("How many friends splitting the bill: "))

#converts tip % to decimal number
tipPercentage = tip/100

#calculates the tip total amount based on the bill
tipAmount = bill * tipPercentage

#calculates the total amount of the bill with the tip included
billAndTip = bill+tipAmount

#calculates the amount each person should pay
finalAmount = billAndTip / people

#truncates the final amount to only 2 decimal points
finalAmount = round(finalAmount, 2)
print(f"Each person should pay {finalAmount}")
