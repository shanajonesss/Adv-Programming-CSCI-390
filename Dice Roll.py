from random import randint
minn = 1
maxx = 6
repeat = True
while repeat:
    user_guess = input("What value are you expecting to see when you roll the dice?: ")
    ## Derrick and I attempted to set boundaries for if user input is greater than 6.. did not work out :-(
    ## but still left that code in here so you know that we still took into account for boundaries
    ## if user_guess < str(6):
        ## print("Your expected value is greater than 6. Please try again.")
    roll = randint(minn,maxx)
    print("Actual result:",roll)
    if user_guess == str(roll):
        print("The expected result and the actual result are the same. Yay!")
    else:
        print("The expected result and the actual result are not the same. Sorry!")
    print("Do you want to roll again?")
    repeat = ("yes") in input().lower()