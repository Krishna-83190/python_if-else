'''
10. Mobile Data Plan Advisor


A telecom company suggests the most suitable data plan based on a user’s daily data usage:

* More than 3GB/day → Premium Plan
* 1GB to 3GB/day → Standard Plan
* Less than 1GB/day → Basic Plan

Write a Python program to recommend a plan.

Input:
Enter daily data usage: 0.8

Output:
Recommended Plan: Basic Plan
'''
dusage = float(input("Enter attendance percentage:"))
if dusage > 3:
	print("Recommended Plan: Basic Plan")
elif dusage >1:
	print("Recommended Plan: standard Plan")
else: 
	print("Recommended Plan: Basic Plan")