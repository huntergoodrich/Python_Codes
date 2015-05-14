print ("Welcome to the Choose your Own Adventure Program!")

print ("You and your friend are walking along the road one day")
print ("You see this dog on the side of the road who looks hurt")
condition = input("What do you do? Help or leave?")
if condition == "Help" or condition ==  "help":
    print ("You've stopped to help")
    print ("The dog's leg is broken")
    condition_1 = input("What do you do to it's leg? Set it, or get it help?")
    if condition_1 == "Set it" or condition_1 == "set it":
        print("You've set the dogs bone correctly, but it seems to be in great pain.")
        print("The dog decides that it hates you for it and bites you and your friend. You both died due to an infection. That's what you get for being a hero.")
    elif condition_1 == "Get it help" or condition_1 == "get it help":
        print("You've decided that your veterinary skills are not up to par and drive it to the nearest clinic.")
        print("You enter the clinic and explain to the techs that this isnt your dog and it needs help.")
        print("The techs also inform you that there will be a $10 fee for walk-ins.")
        condition_2 = input("Do you pay the fee? Yes or no?")
        if condition_2 == "Yes" or condition_2 == "yes":
            print("You are a saint and the dog gets the help that it needs")
            print("You come back and the vet gives you the option of adopting the dog.")
            condition_3 = input("Do you adopt the dog? Yes or no?")
            if condition_3 == "Yes" or condition_3 == "yes":
                print("You have given the dog a nice home.")
                condition_4 = input("What's the dog's gender?(Yes you get a choice)Boy or Girl.")
                if condition_4 == "Girl" or condition_4 == "girl" or condition_4 == "Boy" or condition_4 == "boy":
                    print("You have a lifelong friend.")
            elif condition_3 == "No" or condition == "no":
                print("You have missed out on a great opportunity with mans best friend.")
        elif condition_2 == "No" or condition_2 == "no":
            print("The dog doesn't get treatment and the clinic turns him away out on the street")
            print("Way to go.")
elif condition == "Leave" or condition == "leave":
    print ("You've chose to go on your own way")
    






    
