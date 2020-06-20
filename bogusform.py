# Numbers Processor

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    if line ==" " or "" or None:
        print("It's an empty line")
    else:
        for substr in strings:
            total += float(substr)
            print("The total is:", total)
except:
    print(substr, "is not a number.")
