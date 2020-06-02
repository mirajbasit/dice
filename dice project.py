import random
# do this cuz u have to
def main():

    # .lower makes everything inputted lowercase
    roll_dice = input("Would you like to roll a dice, yes or no? ").lower() 

    # add the name of what is being defined each time
    if roll_dice == "no" or roll_dice == "n":
        print("Ok, see you later ")
    
    elif roll_dice == "yes" or roll_dice == "y":
        yeppers = True
        #you do not have to put the == true, still put the colon cuz loop
        while yeppers == True:
            outcome = random.randint(1,6)
            print(f"The result is  {outcome}")

            re_roll =   input("Will you roll again? ").lower()

            if re_roll == "no" or re_roll == "n":
                print("Ok, thanks for playing ")
                yeppers = False
            
            elif re_roll == "yes" or re_roll == "y":
                yeppers = True
            else:
                print("Please enter yes or no! ")
                #place for each condition
                yeppers = False
            
    
    else:
        print("Please try again ")
    



# do this cuz u have to
if __name__ == "__main__":
    main()