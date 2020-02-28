#Exercise 3.1 - a program to prompt the user for hours and rate per hour using input to compute gross pay
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
pay = -1
if h <= 40:
    pay = h * r
    print("Pay:",pay)
else:
    # pay = r * 40 + (h - 40) * 1.5 * r
    # Method 1
    reg = 40 * r
    otp = (h - 40) * r * 1.5
    pay = reg + otp
    # Method 2
    print("Pay:",pay)
#Calculate the gross pay depending on if hours were above 40 or not