while True:
    wrd=input("Enter the word required")
    if wrd == "password":
        print("You've sucessfully got out of the loop")
        break
    
    
userWord=input("Enter a word here: ")
userWord=userWord.upper()

for letter in userWord:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    print(letter)
