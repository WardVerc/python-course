print('''

                                         =||=   
                         o   |\ ,'`. /||\ ,'`. /|    o     
 _   _   _   |\__      /\^/\ | `'`'`' || `'`'`' |  /\^/\   |\__     _   _   _ 
| |_| |_| | /   o\__  |  /  ) \      /  \      /  |  /  ) /   o\__ | |_| |_| |
 \       / |    ___=' | /  /   |    |    |    |   | /  / |    ___=' \       / 
  |     |  |    \      Y  /    |    |    |    |    Y  /  |    \      |     |
  |     |   \    \     |  |    |    |    |    |    |  |   \    \     |     |  
  |     |    >    \    |  |    |    |    |    |    |  |    >    \    |     |  
 /       \  /      \  /    \  /      \  /      \  /    \  /      \  /       \ 
|_________||________||______||________||________||______||________||_________|
    __         __       __       __        __       __       __         __   
   (  )       (  )     (  )     (  )      (  )     (  )     (  )       (  )  
    ><         ><       ><       ><        ><       ><       ><         ><   
   |  |       |  |     |  |     |  |      |  |     |  |     |  |       |  |  
  /    \     /    \   /    \   /    \    /    \   /    \   /    \     /    \ 
 |______|   |______| |______| |______|  |______| |______| |______|   |______|
      _       _        _                     _                     
     / \     (_)      (_)                   (_) _   _              
    |  | _/_  /        /  / _       ,        /.' ).' )             
    | /  /      ,     /  / / )_/ / / )      /   /   /  _       _   
  .-|/--'|     / )   (__/,(_/ (_/\/ (__    /   /   /  / )_/ /_/_)  
 (__/\_   \_  /_/    __/'                 /   /   (__(_/ (_/ (__  () () ()      

      
''')

print("Welcome to the Chess Adventure!\n")
print("You wake up and have chessboard in front of you. Magnus Carlsen is sitting in front of you. He says it's your move.")
print("Make a random move? Press y.")
first_action = input("Ask Magnus why you are here and how you can go home? Press n.").lower()
if first_action == "y":
    print("You sacrificed your queen. Magnus laughs with a big ego, he forgot that he was eating and he chokes.")
    print("Magnus is no more. What do you do now?")
    print("Press y if you want to go through the door.")
    second_action = input("Press n if you want to go through the hole in the wall.").lower()
    if second_action == "y":
        print("You are outside the strange house. There is a horse and a red Ferrari.")
        third_action = input("Press y to pet the horse, press n to get in the Ferrari.").lower()
        if (third_action == "n"):
            print("You escaped with a nice Ferrari! You win!")
        else:
            print("The horse kicks you in the balls. You had so much pain you died. You died.")
    else:
        print("The hole is filled with rats. They ate you alive. You died.")
else:
    print("You suddenly fell in a hole. You died.")