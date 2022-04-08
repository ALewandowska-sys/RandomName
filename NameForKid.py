import random


def draw():
  sex = input("Choose a sex for child (boy, girl): ")
  
  if sex == 'boy':
    print("\nIt will be: " + random.choice(open('boys.txt' , 'r').readlines()).strip() + "!\n")
  elif sex == 'girl':
    print("\nIt will be: " + random.choice(open('girls.txt', 'r').readlines()).strip() + "!\n")
  else:
    print("I don't understand")
    



print("Do you thinking about a name for your future child? We can help you!")

while True:
  user_choice = input("Ready to draw a los? (yes/no) ")
  if user_choice == 'yes':
    draw()
  
  elif user_choice == 'no':
    print("Thanks for participation!")
    break

  else:
    print("I don't understand... try again")
