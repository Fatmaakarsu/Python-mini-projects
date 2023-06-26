# Hangman game simple version

word = "Python"

lives = len(word)

# to keep the letters the user entered
emptyList = []

# at the beginning of the game, it prints this on the screen.
for i in word:
  print("-")

for i in range(len(word)):

    
    input1 = input("Guess a letter: ")
    emptyList.append(input1)
    if input1 in word:
        print("Correct.")

       
    else:
        print(f"Wrong! Your left lives: {lives-1}")
        
    lives -= 1

    for i in word:
          if i in emptyList:
            print(i)
          else:
            print("-")

    if lives == 0:
        print("Game over!")
        break





