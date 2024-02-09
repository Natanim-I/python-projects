print('''
       _,--._.-,                                 
      /\_r-,\_ )                                 
   .-.) _;='_/ (.;                            
    \ \'     \/S )                              
     L.'-. _.'|-'                               
    <_`-'\'_.'/                                    
      `'-._( \                                     
             \\       ___               
              \\   .-'_. /               
               \\ /.-'_.'                   
                \('--'	                         
           snd    \                         

''')
is_dog_found = False
print("                     Welcome to Choose Your Own Adventure Game!")
print("------------------------------------------------------------------------------------------------------------------")
print("     It is a winter time and you are out walking your Dog :). Your dog runs and disappeared from you ")
print("     but you saw going into a large house. You followed him, It was getting late and it started to rain.")
print("     Inside the house you saw a beautiful girl: ")
choice1 = input("       What do you do talk to her or say nothing? ").lower()
if choice1 == "talk":
    print("     You asked her name and she smiled :) and told you. You also asked her age: ")
    choice2 = int(input("       How old are you? "))
    if choice2 >= 18:
        choice3 = input("       Should you ask for her number? ").lower()
        if choice3 == "yes":
            print("     You got her number, she invited you to have a drink with her: ")
            choice4 = input("       Should you get a drink? ")
            if choice4 == "yes" and is_dog_found:
                print("     You found your Dog and Get the girl you can give her the rose :) You WON!!!")
            elif  is_dog_found and choice4 == "no":
                print("     You found your dog but declined the girl. She doesn't want you anymore!!!")
                print("     Game Over, rose wasted!!!")
            else:
                print("     You told her about your dog and she offered to help ;). You are looking for your dog together.")
                choice5 = input("       Should you bark or whistle? ").lower()
                if choice5 == "whistle":
                    print("     Your dog heard your whistle and started barking. WOOO WOO.")
                    print("     She saw your dog and found your dog!!!")
                    print("     You ask and took the girl on a Date!!! You WON :).")
                    is_dog_found = True
                else:
                    print("     Time over, only dogs bark. You LOST!!!")
        else:
            print("     Game Over You missed the chance to meet her again :(!")
    else:
        print("     Game Over, Under age!!!")
else:
    print("     Game Over You missed the girl! The rose is useless :(!")

if is_dog_found:
    print("###########################################################################################")
    print('''
           _,--._.-,                                 
          /\_r-,\_ )                                 
       .-.) _;='_/ (.;                            
        \ \'     \/S )                              
         L.'-. _.'|-'                               
        <_`-'\'_.'/                                    
          `'-._( \                                     
                 \\       ___               
                  \\   .-'_. /               
                   \\ /.-'_.'                   
                    \('--'	                         
               snd    \                         

    ''')
    print("###########################################################################################")