score = input("Enter Score: ")
try:
    s = float(score)
except:
    print("Please enter numeric value.")
    quit()

if s >= 1.0 :
    print("Out of range.")
    quit()
elif s >= 0.9 :
    grade = "A"
elif s >= 0.8 :
    grade = "B"
elif s >= 0.7 :
    grade = "C" 
elif s >= 0.6 :
    grade = "D"
elif s < 0.6 :  
    grade = "F"

print(grade)