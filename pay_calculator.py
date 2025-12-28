#create a function to calculate the pay
def computepay(h, r):
    if h <= 40 :
        p = h * r
    else :
        p = 40 * r + (h - 40) * r * 1.5
    return p

#Enter the hours and rate, remember to convert the input into float
hrs = input("Enter Hours:")
hr = float(hrs)
rate = input("Enter Rate:")
rt = float(rate)
p = computepay(hr, rt)
print("Pay", p)