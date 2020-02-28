#Excercise 4.6 - Write a program to prompt the user for hours and rate per hour using input to compute gross pay - with a computepay() function
def computepay(h,r):
    h = float(hrs)
    r = float (rate)
    if h <= 40:
        p = h * r
        return p
    else:
        reg = 40 * r
        otp = (h-40) * r * 1.5
        p = reg + otp
        return p
#Defined a function which compute the gross pay by given hours & rate - computepay()

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    pay = computepay(hrs,rate)
    print("Pay:",pay)
except:
    print("Error, please enter numeric input")
#Read and validate the input from user, and call the coomputepay() function
