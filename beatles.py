beatles=[]
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for i in range (0,2):
    beatles.append(input("Enter new members: "))
print("Step 3:", beatles)

print(len(beatles))
del beatles[3]
del beatles[3]
print("Step 4:", beatles)

beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
