num = 6
count = 0
list = ["d", "o", "g"]
print("Play hangman with me! The word if three letters long and it is an animal. You can only get six incorrect!")
while count != 3 and num!= 0:
    guess = input("Guess, one letter at a time")
    if guess in list:
        print("correct")
        if guess == list[0]:
            print("find the remaining letters d--")
            count += 1
        if guess == list[1]:
            print("find the remaining letters -o-")
            count += 1
        if guess == list[2]:
            print("find the remaining letters --g")
            count += 1
    else:
        print("incorrect")
        num -= 1
if num == 0:
    print("You lose!")
print(" ________")
print(" |      |")
print(" |    (X_X)")
print(" |     \||/")
print(" |      /\ ")
print("_|_ ")
if count == 3:
    print("You got it! The word is dog")
    
