hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hrm=mins+dura
nhr=hrm//60
mhr=hrm%60

fh=hour+nhr
while (fh>23):
    if (fh>23):
        fh=fh-24
print("End time (hrs) is ",fh)
print("End time (mins) is ",mhr)
print("\nThank you folks")
