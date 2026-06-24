'''
12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680
'''
bill = int(input("Enter bill amount:"))
if bill <= 1000:
	final = bill + bill*5//100
elif bill <= 5000 :
	final = bill + bill*12//100
	if bill > 3000:
		final +=200
elif bill >= 5000 :
	bill +=200
	final = bill + bill*18//100
print("Final Bill Amount:",final)
