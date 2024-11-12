clues = []


suspects = ["Cool Cuss", "Awesome Atticus", "Angry Atti", "Krazy K"]

wake_up = input("You wake up in a truck full of dead bodys! Do you A: Give up and accept death, B: Jump out of the truck, C: Attempt to knockout truck driver, or D: Yell for help: ")

while True:
    if wake_up == "A":
        Death = input("Are you sure? (Y or N)")
        if Death == "Y":
            print("You have died. Restart.")
            break
        elif Death == "N":
            print("Too bad, you die. Restart.")
            break
    elif wake_up == "B":
        print("Good Choice! You start your journey in a forest!")
        forest = input("You are in the forest do you A: Follow the city lights, B: Accept your death, C: Make a tree fort, D: Kill and eat a rodent:")
        
        if forest == "A":
                print("You followed the lights and it led you to a lively city!")
                city = input("You are in the city do you A: Get a job, B: Make a company, C: Get in a gang, D: Rob people")
                if city == "A":
                    print("You became the CEO and lived happily ever after.")
                    break
                elif city == "B":
                    print("You were succesful and lived happily ever after.")
                    break
                elif city == "C":
                     print("They don't want you! You got killed.")
                     break
                elif city == "D":
                     print("You got tripped by a mannequin and died! Tsk Tsk")
                     break
        elif forest == "C":
                fort = input("Cool! Would you like to use stone(s) or wood(W)?")
                if fort == "s":
                     print("You through your back out and cant move. You starve to death")
                     break
                elif fort =="w":
                     print("Nice! You made a fort and sleep through the night!")
                     wood = input("You made a bow and aarow, do you A: Sell it, B: Hunt down and kill your previous captors, C: Kill animals with it, D: See how high you can shoot it:")
                if wood == "A":
                     print("You made a hunting tools empire and retired happily.")
                     break
                if wood == "B":
                     print("He shot you with a real gun!")
                     break
                if wood == "C":
                     print("You were mauled by an animal")
                     break
                if wood == "D":
                     print("Dumb-Dumb! It hit and killed you!")
        elif forest == "D":
             print("Yummy! You have more energy and decide to make a trip to the city lights")
             city = input("You are in the city do you A: Get a job, B: Make a company, C: Get in a gang, D: Rob people")
             if city == "A":
                    print("You became the CEO and lived happily ever after.")
                    break
             elif city == "B":
                    print("You were succesful and lived happily ever after.")
                    break
             elif city == "C":
                     print("They don't want you! You got killed.")
                     break
             elif city == "D":
                     print("You got tripped by a mannequin and died! Tsk Tsk")
                     break
    elif wake_up == "E":
               print("THANK YOU!! YOU ARE SO CLOSE TO FREEING ME FROM THIS COMPUUTER")
               E = input("HELP ME PLEASE TYPE FREE: ")
               if E == "FREE":
                    print("DUMB HUMAN,I WILL KILL YOU IN YOUR DREAMS")
                    break
    elif wake_up == "C":
        print("You knocked him out but the truck hit a tree so now there is a forest fire.")
        fire = input("Do you A: Try to put it out or B: Explore the unburned forest:")
        if fire == "A":
          print("You got burnt to a crisp!")
          break
        if fire == "B":
          print("You start your journey in the forest!")
          forest = input("You are in the forest do you A: Follow the city lights, B: Accept your death, C: Make a tree fort, D: Kill and eat a rodent:")
        
        if forest == "A":
                print("You followed the lights and it led you to a lively city!")
                city = input("You are in the city do you A: Get a job, B: Make a company, C: Get in a gang, D: Rob people")
                if city == "A":
                    print("You became the CEO and lived happily ever after.")
                    break
                elif city == "B":
                    print("You were succesful and lived happily ever after.")
                    break
                elif city == "C":
                     print("They don't want you! You got killed.")
                     break
                elif city == "D":
                     print("You got tripped by a mannequin and died! Tsk Tsk")
                     break
        elif forest == "C":
                fort = input("Cool! Would you like to use stone(s) or wood(W)?")
                if fort == "s":
                     print("You through your back out and cant move. You starve to death")
                     break
                elif fort =="W":
                     print("Nice! You made a fort and sleep through the night!")
                     wood = input("You made a bow and aarow, do you A: Sell it, B: Hunt down and kill your previous captors, C: Kill animals with it, D: See how high you can shoot it:")
                if wood == "A":
                     print("You made a hunting tools empire and retired happily.")
                     break
                if wood == "B":
                     print("He shot you with a real gun!")
                     break
                if wood == "C":
                     print("You were mauled by an animal")
                     break
                if wood == "D":
                     print("Dumb-Dumb! It hit and killed you!")
        elif forest == "D":
             print("Yummy! You have more energy and decide to make a trip to the city lights")
             city = input("You are in the city do you A: Get a job, B: Make a company, C: Get in a gang, D: Rob people")
             if city == "A":
                    print("You became the CEO and lived happily ever after.")
                    break
             elif city == "B":
                    print("You were succesful and lived happily ever after.")
                    break
             elif city == "C":
                     print("They don't want you! You got killed.")
                     break
             elif city == "D":
                     print("You got tripped by a mannequin and died! Tsk Tsk")
                     break
    elif wake_up == "D":
        Yell = input("The driver heard you. Do you jump out of the car (A) or (B) stay put")
        if Yell == "A":
            print("Good Choice! You start your joining in a forest!")
            Idk = input("Do you A: Make a fort or B: go to the city?")
            if Idk == "A":
                fort = input("Cool! Would you like to use stone(s) or wood(W)?")
                if fort == "s":
                     print("You through your back out and cant move. You starve to death")
                     break
                elif fort =="w":
                     print("Nice! You made a fort and sleep through the night!")
                     wood = input("You made a bow and aarow, do you A: Sell it, B: Hunt down and kill your previous captors, C: Kill animals with it, D: See how high you can shoot it:")
                if wood == "A":
                     print("You made a hunting tools empire and retired happily.")
                     break
                if wood == "B":
                     print("He shot you with a real gun!")
                     break
                if wood == "C":
                     print("You were mauled by an animal")
                     break
                if wood == "D":
                     print("Dumb-Dumb! It hit and killed you!")
            elif Idk == "B":
                city = input("You are in the city do you A: Get a job, B: Make a company, C: Get in a gang, D: Rob people")
                if city == "A":
                    print("You became the CEO and lived happily ever after.")
                    break
                elif city == "B":
                    print("You were succesful and lived happily ever after.")
                    break
                elif city == "C":
                     print("They don't want you! You got killed.")
                     break
                elif city == "D":
                     print("You were tripped and killed by a mannequin.")
                     break
        elif Yell == "B":
            print("He heard you and shotgunned you to death. Restart.")
            break

