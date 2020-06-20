blocks = int(input("Enter the number of blocks: "))
height=0
while blocks>0:
    blocks-=height
    height+=1
print("The height of the pyramid:", height)
