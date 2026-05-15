print("welcome to hangman!!!\n")
print("Note:Before we start the game, choose a number so thet word for the game can be selected\n")
words=["banana","kivi","mango","grape"]

for i in range(len(words)):
    print(f"{i+1}. word{i+1}")

choice = int(input("choose an option(1-4): "))
word = words[choice - 1]

print("\nlets start the game!!!\n")

display=["_"]*len(word)
print(display)

life=6
while life>0:
    print(display)
    guess=input("enter the letter:").lower()

    if guess in word:
        print("correct guess!\n")
        for i in range(len(word)):
            if word[i]== guess:
                display[i]=guess
    else:
        print("oops! wrong guess\n")
        life -= 1
        print("Lives left:",life)
    if "_" not in display:
     print(display)
     print("you have won the game!")
     break

if life == 0:
    print("you lost! The word was:", word)


