print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print('You\'re in a crossroad. Which direction do you want to go?\n'
      'Type Left or Right.')

choice_1 = input().lower()

if choice_1 == "left":
    print("You\'ve come to a lake. What do you want to do?\n"
          "Type Swim or Wait")

    choice_2 = input().lower()
    if choice_2 == 'wait':
        print('A boat has come. By which door you want to go in?\n'
              'Type Red or Blue or Yellow')

        choice_3 = input().lower()
        if choice_3 == 'red':
            print('Game over. You\'re burned by fire')
        elif choice_3 == 'blue':
            print('Game over. You\'re eaten by beast')
        elif choice_3 == 'yellow':
            print('Congratulations. You\'ve found the treasure.')
        else:
            print('Game over. You did\'nt follow the instruction')


    elif choice_2 == 'swim':
        print('Game over. You\'re attacked by crocodile')
    else:
        print('Game over. You did\'nt follow the instruction')

elif choice_1 == 'right':
    print('Game over. You fell into a hole')

else:
    print('Game over. You did\'nt follow the instruction')


