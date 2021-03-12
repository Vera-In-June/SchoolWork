import random


# this is main, everything goes here.
# it starts with run_name_go()
# every time it will query run_game_again
# this will not stop until run_again_bool is returned as False
def main():
    right_name_go()
    while True:
        run_game_again_bool = run_game_again()
        if run_game_again_bool:
            right_name_go()
        else:
            return

# nostolima is a strange emotion, I don't know what other name it has so I'm using my own until further notice
feels_dysphoric_quotes = ["A woman is her mind, she is eternal beyond body",
                          "For you have known yourself since the beginning, the whole world is but a morsel in your life"]
feels_nostolomic_quotes = ["This too shall pass", "They know you not, how can they know that which is untold?", "You are young, and your bitter recollections have time to change themselves into sweet remembrances"]
feels_lonely_quotes = ["Souls are alone indefinitely, though paths cross when sighing breaks", "The more we venture the more we gain, if we know how to wait"]
feels_depressed_quotes = ["Life is a chaplet of little miseries which the philosopher surveys with a smile"]


def name_getter():
    username = input("what is your name, stranger? ")
    if username.isalpha():
        if username in ['Liam', 'Rohan', 'Sebastian', 'Wilhelm']:
            print("girl, you know that isn't you...")
            return
        else:
            print(
                f"\nHello {username}, I know why you are here.\n\nhmm...\n\nI'm guessing that you would be feeling dysphoric, nostolomic, lonely, or just plain depressed, correct?\n")
    else:
        print("that doesn't appear to be your name...")
        return
    user_feels = input("I'm feeling ")
    user_feel = user_feels.upper()
    if user_feel.isalpha() is False:
        print("Speak not in these strange tongues and wingdings!")
        return
    return username, user_feel


# please don't make fun of me, I can't help but make my programs sound sad
def run_game_again():
    runs_again = ''
    run_again_bool = False
    while runs_again == '':
        runs_again = input('\nWant to go again, friend? Y/N ')
        run_again = runs_again.upper()
        if run_again == 'Y':
            run_again_bool = True
            print(f"\nI'll begin again, friend...\n")
        elif run_again == 'N':
            run_again_bool = False
            print("\nI'm glad we could chat, friend...\n")
        elif len(run_again) > 1 or run_again.isalpha() is False:
            print('\nthat is an invalid answer')
            runs_again = ''
            continue
    return run_again_bool


def right_name_go():
    try:
        username, user_feel = name_getter()
    except TypeError:
        return
    if user_feel not in ['DYSPHORIC', 'NOSTOLOMIC', 'LONELY', 'DEPRESSED']:
        print("sorry, I can't help with that...")
        return
    else:
        if user_feel == "DYSPHORIC":
            print(random.choice(feels_dysphoric_quotes))
        elif user_feel == "NOSTOLOMIC":
            print(random.choice(feels_nostolomic_quotes))
        elif user_feel == "LONELY":
            print(random.choice(feels_lonely_quotes))
        elif user_feel == "DEPRESSED":
            print(random.choice(feels_depressed_quotes))

# Big ups Hamish and Jackson for teaching me about some things that I used in this code

if __name__ == '__main__':
    main()
