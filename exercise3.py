game = 'playing'
restart = 0
while True:
    print("You are Ollie, a likeable young guy in search of love. Our story begins when Ollie comes across an attractive")

    user_response = input("Will you swipe left or right?: (1)Right (2)Left >").lower().strip()
    if 'right' in user_response:
        print("She swiped right, too! It's a match! Now don't screw this up...")
    elif 'left' in user_response:
        print("Hmm, perhaps Ollie's standards are a little high...")
        replay = input('would you like to play again? (1)yes (2)no >').lower().strip()
        if 'yes' in replay:
            print('From the top lads, good luck')
            restart = 1
        elif 'no' in replay:
            break
            print('game over')

    if restart == 1:
        restarting = True
    else:
        print("She messages you and asks for a date! But she wants you to pick the type of restaurant.")
        food_response = input("What kind of food will you choose?: (1)Italian (2)Curry (3)Pub grub >").lower().strip()
        if 'italian' in food_response:
            print("Ah, molto bella!")
        elif 'curry' in food_response:
            print("Curry on a first date!? What were you thinking? GAME OVER")
            replay = input('would you like to play again? (1)yes (2)no >').lower().strip()
            if 'yes' in replay:
                print('From the top lads, good luck')
                restart = 1
            elif 'no' in replay:
                break
                print('game over')
        elif 'pub' in food_response:
            print("Lovely jubbly.")

    if restart == 1:
        restarting = True
    else:
        print("You meet at the restaurant and after an hour, everything seems to be going fine! However, you notice your date might have had a bit much to drink...")
        drunk_guess = input(" what do you think? (Enter true or false) >").lower().strip()
        print("Whatever you say! Oh no, now she's asking how old you think she is!"
            " Maybe she's had too much drink to really notice what you say...")
        age_input = input("What age will you say?")
        if age_input < '30' or 'true' in drunk_guess:
            print("She smiles and shrugs. 'I'll never tell!' Phew, that was a close one!")
        elif age_input >= 30 and 'false' in drunk_guess:
            print("Uh, I think you might have miscalculated somewhere... GAME OVER")
            replay = input('would you like to play again? (1)yes (2)no >').lower().strip()
            if 'yes' in replay:
                print('From the top lads, good luck')
                restart = 1
            elif 'no' in replay:
                break
                print('game over')

    if restart == 1:
        restarting = True
    else:
        print("The rest of the evening goes wonderfully and soon, the bill arrives. Yikes! £100!?")
        offer = input("(1)Say you left your wallet at home. (2)Offer to pay. >")
        money = input("Wait... how much money do you actually have? >")
        if 'left' in offer:
            print("Sorry, nobody likes a cheapskate.")
            if 'yes' in replay:
                print('From the top lads, good luck')
                restart = 1
            elif 'no' in replay:
                break
                print('game over')
        elif 'offer' in offer and money >= '100':
            print("How very gallant of you! She seems impressed...")
    if restart == 1:
        restarting == True
    else:
        print('congratulations you have successfully completed a date')
        game = 'won'
        break