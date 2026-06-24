'''
15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220
'''
vehicle = input("Enter vehicle type: ")
hrs = int(input("Enter hours parked:"))

if vehicle == "Bike":
    rate = 10
elif vehicle == "Car":
    rate = 20
elif vehicle == "Bus":
    rate = 50
else:
    print("Invalid Vehicle Type")
    

fee = rate * hrs

if hrs > 5:
    fee += 100

print("Total Parking Fee: ₹",fee)

