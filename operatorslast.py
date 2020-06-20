x = float(input("Enter value for x: "))

y=1/(x+1/(x+1/(x+1/x)))

print("y =", y)

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hrm=mins+dura
nhr=hrm//60
mhr=hrm%60

print("End time (hrs) is ",12+nhr)
print("End time (mins) is ",mhr)
print("\nThank you folks")
