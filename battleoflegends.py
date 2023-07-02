import time
import random

print (
    """
    
                                         (                                  
   (           )   ) (            (      )\ )                       (       
 ( )\     ) ( /(( /( )\  (        )\ )  (()/(   (  (  (    (        )\ )    
 )((_) ( /( )\())\()|(_)))\    ( (()/(   /(_)) ))\ )\))(  ))\ (    (()/((   
((_)_  )(_)|_))(_))/ _ /((_)   )\ /(_)) (_))  /((_|(_))\ /((_))\ )  ((_))\  
 | _ )((_)_| |_| |_ | (_))    ((_|_) _| | |  (_))  (()(_|_)) _(_/(  _| ((_) 
 | _ \/ _` |  _|  _|| / -_)  / _ \|  _| | |__/ -_)/ _` |/ -_) ' \)) _` (_-< 
 |___/\__,_|\__|\__||_\___|  \___/|_|   |____\___|\__, |\___|_||_|\__,_/__/ 
                                                  |___/                     

    """
)

sasuke = "Sasuke"
guts = "Guts"
shinakuma = "Shin Akuma"

sasuke_hp = 170
guts_hp = 250
dio_hp = 300
shinakuma_hp = 600


sasuke_damage = random.randint(20, 150)
guts_damage = random.randint(30, 200)
dio_damage = random.randint(40, 160)
shinakuma_damage = random.randint(70, 600)

while True:
    while True:
        print("1)    Sasuke")
        print("2)    Shin Akuma")
        print("3)    Guts")
        print("4)    Quit")
        user_selection = input("Choose your character:")
        if user_selection == "1":
            my_character = sasuke
            my_hp = sasuke_hp
            my_damage = sasuke_damage
            break
        elif user_selection == "2":
            my_character = shinakuma
            my_hp = shinakuma_hp
            my_damage = shinakuma_damage
            break
        elif user_selection == "3":
            my_character = guts
            my_hp = guts_hp
            my_damage = guts_damage
            break
        elif user_selection == "4":
            break
        else:
            print("Selection is not valid, Try again")
    print(f"User has selected {my_character}, with health of {my_hp}hp and damage of {my_damage}")
    dio_hp = 300
    my_hp = my_hp
        

    while True:
        if my_hp <= 0:
            break
        elif dio_hp <0:
            break
        else:
            dio_hp - my_damage
            print(f"{my_character} has damaged Dio! ")
            time.sleep(5)
            dio_hp = dio_hp - my_damage
            if dio_hp <= 0:
                print(f"Dio has lost the battle! Defeated by {my_character}")
                if my_character == sasuke:
                    print ("Sasuke: If anyone wants to deny my way of living, I'll kill everyone they ever cared about. Maybe then they'll understand... a little bit of my hatred.")
                    play_again = int(input("Press 1 to play again, 0 to exit. "))
                    if play_again == 0:
                        break
                elif my_character == guts:
                    print ("Guts: I'd rather fight for my life than live it.")
                    play_again = int(input("Press 1 to play again, 0 to exit. "))
                    if play_again == 0:
                        break
                elif my_character == shinakuma:
                    print ("Shin Akuma: Now you know the wrath of the Satsui No Hadou!!")
                    play_again = int(input("Press 1 to play again, 0 to exit. "))
                    if play_again == 0:
                        break
            elif dio_hp >= 0:
                print(f"Dio's turn, current health: {dio_hp}hp")
                print("Dio: The World's power and precision are both superior! I've seen enough. I'm satisfied. I will end you now!")
                time.sleep(5)
                my_hp = my_hp - dio_damage
                print(f"Dio has attacked leaving you with {my_hp}hp")
                if my_hp <= 0:
                    print(f"{my_character} has been defeated! Dio wins!")
                    play_again = int(input("Press 1 to play again, 0 to exit. "))
                    if play_again == 0:
                        break 

        

