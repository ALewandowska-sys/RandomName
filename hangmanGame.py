import random

user_word = []
user_letters = []
life = 6
word = random.choice(open('girls.txt', 'r').readlines()).strip()
theme = "Female name"

print("Welcone in the Hangman Game!\nYou have only", life, "lifes\nLet's go!\n\nCategory: ", theme)

def find_indexes(word, letter):
  indexes = []
  for index, letter_in_word in enumerate(word):
    if letter == letter_in_word:
      indexes.append(index)
  return indexes


for _ in word:
    user_word.append("_") 



while True:
  print(" ".join(user_word))
  print()
    
  if "".join(user_word) == word:
    print("Congratulation, You win!")
    break

  letter = input("Suggested letter: ")
  found_indexes = find_indexes(word, letter)

  if letter in user_letters:
    print("You tried it before!")
  
  else:
    user_letters.append(letter)
    
    if len(found_indexes) == 0:
      life -= 1
      
      if life == 0:
        print("You lose! You didn't guess: ", word)
        break
      
      print("Wrong answer. Now you have only", life, "lifes...") 
    
    else:
      for index in found_indexes:
        user_word[index] = letter
