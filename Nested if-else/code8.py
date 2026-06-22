'''
8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500
'''
u1 = int(input("Unit1 = "))
u2 = int(input("Unit2 = "))
u3 = int(input("Unit3 = "))
u4 = int(input("Unit4 = "))
u5 = int(input("Unit5 = "))
u6 = int(input("Unit6 = "))

highest = u1

if u2 > highest:
    highest = u2

if u3 > highest:
    highest = u3

if u4 > highest:
    highest = u4

if u5 > highest:
    highest = u5

if u6 > highest:
    highest = u6

print("Highest Stock =", highest)