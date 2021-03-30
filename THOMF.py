# The House of my Father, text based (meta?) psychological horror game in a strange church
# 你好，我很高兴认识你！你很害怕吗？
import time

def play_game_y_n():
    time.sleep(0.4)
    play_yah_nah = input("> would you like to play? ")
    play_yay_nay = play_yah_nah.upper()
    if play_yay_nay == "NO":
        time.sleep(0.4)
        print("> you can't stay away forever")
        quit()
    elif play_yay_nay == "YES":
        return
    else:
        time.sleep(0.4)
        print("> type 'yes' or 'no' for your answer")
        play_game_y_n()

def play_with_style():
    time.sleep(0.4)
    hit_enter = input("> ")
    if hit_enter.isalnum():
        return
    else:
        return
    # lol this is very funny code

time.sleep(0.4)
print(">  _______ _    _ ______  _    _  ____  _    _  _____ ______   ____  ______ ")
time.sleep(0.4)
print("> |__   __| |  | |  ____|| |  | |/ __ \| |  | |/ ____|  ____| / __ \|  ____|")
time.sleep(0.4)
print(">    | |  | |__| | |__   | |__| | |  | | |  | | (___ | |__   | |  | | |__   ")
time.sleep(0.4)
print(">    | |  |  __  |  __|  |  __  | |  | | |  | |\___ \|  __|  | |  | |  __|  ")
time.sleep(0.4)
print(">    | |  | |  | | |____ | |  | | |__| | |__| |____) | |____ | |__| | |     ")
time.sleep(0.4)
print(">    |_|  |_|  |_|______||_|  |_|\____/ \____/|_____/|______| \____/|_|     ")
time.sleep(0.4)
print(">          __  ____     __ ______   _______ _    _ ______ _____  ")
time.sleep(0.4)
print(">         |  \/  \ \   / /|  ____/\|__   __| |  | |  ____|  __ \ ")
time.sleep(0.4)
print(">   ----- | \  / |\ \_/ / | |__ /  \  | |  | |__| | |__  | |__) | -----")
time.sleep(0.4)
print(">   ----- | |\/| | \   /  |  __/ /\ \ | |  |  __  |  __| |  _  /  -----")
time.sleep(0.4)
print(">   ----- | |  | |  | |   | | / ____ \| |  | |  | | |____| | \ \  -----")
time.sleep(0.4)
print(">         |_|  |_|  |_|   |_|/_/    \_\_|  |_|  |_|______|_|  \_/")

play_game_y_n()
time.sleep(0.4)
print("> You find yourself at the gate of an old church, how you came to be here you are unsure,")
time.sleep(2)
print("> yet here you are all the same. You know not your name, as you know not why the wind howls so.")
time.sleep(2)
print("> How will you remedy this offence?")

play_with_style()
time.sleep(0.4)
print("> A) look around")
time.sleep(0.7)
print("> B) try the gate")
time.sleep(0.7)
print("> C) lay down")
time.sleep(0.9)
print("> D) forgive yourself")

def taron():
    time.sleep(0.4)
    print("> will you enter the sacristy?")
    time.sleep(0.4)
    sacristy_entered = input("> ")
    sacristy_enter = sacristy_entered.upper()
    if sacristy_enter not in ['YES', 'NO']:
        time.sleep(0.4)
        print("> you are under the illusion of choice, for you know you must eventually")
        taron()
    elif sacristy_enter == 'YES':
        time.sleep(0.4)
        print("> in the cramped and dusty room you find a trapdoor with a broken padlock and a crowbar")
        time.sleep(0.4)
        print("> do you take the crowbar?")
        crow_deny = False
        def crowbar_phase(crow_deny):
            time.sleep(0.4)
            crowtaker = input("> ")
            crowtaken = crowtaker.upper()
            if crowtaken not in ['YES', 'NO']:
                time.sleep(0.4)
                print("> type 'yes' or 'no' for your answer")
                crowbar_phase(crow_deny)
            elif crowtaken == 'YES':
                time.sleep(0.4)
                print("> you take the cold metal shaft and descend into the dusty cell.")
                time.sleep(0.4)
                print("> this is where your father put you on Sundays.")
                time.sleep(0.4)
                print("> all you had was a photo of him.")
                time.sleep(0.4)
                print("> and ", end=''), time.sleep(0.5), print("he ", end=''), time.sleep(0.5), print("made ", end=''), time.sleep(0.5), print("you ", end=''), time.sleep(0.5), print("worship ", end=''), time.sleep(0.5), print("it")
                time.sleep(0.4)
                print("> will you smash his worthless portrait into tiny, pathetic smithereens?")
                try_answer = False
                def smash_fight(try_answer):
                    time.sleep(0.4)
                    smash_yes_no = input("> ")
                    smash_y_n = smash_yes_no.upper()
                    if try_answer == False and smash_y_n != "I WILL SMASH HIS WORTHLESS PORTRAIT AND CONTINUE LIVING":
                        time.sleep(0.4)
                        print("> I DON'T CARE! SAY IT")
                        try_answer = True
                        smash_fight(try_answer)
                    elif smash_y_n != "I WILL SMASH HIS WORTHLESS PORTRAIT AND CONTINUE LIVING" and try_answer == True:
                        time.sleep(0.4)
                        print("> COME ON! SAY IT! SAY 'I WILL SMASH HIS WORTHLESS PORTRAIT AND CONTINUE LIVING'")
                        smash_fight(try_answer)
                    elif smash_y_n == "I WILL SMASH HIS WORTHLESS PORTRAIT AND CONTINUE LIVING" and try_answer == False:
                        time.sleep(0.4)
                        print("> .", end=""), time.sleep(0.8), print(".", end=""), time.sleep(0.8), print(".")
                        time.sleep(1)
                        print("> you did it"), print("> .", end=""), time.sleep(0.8), print(".", end=""), time.sleep(0.8), print(".")
                        time.sleep(1)
                        print("> you can go home now")
                        time.sleep(1)
                        print("> please, forgive yourself")
                        time.sleep(1)
                        print("> you can wake up now...")
                        time.sleep(2)
                        print("TERMINATE CONNECTION")
                        time.sleep(1)
                        quit()
                    elif smash_y_n == "I WILL SMASH HIS WORTHLESS PORTRAIT AND CONTINUE LIVING" and try_answer == True:
                        time.sleep(0.4)
                        print("> .", end=""), time.sleep(0.8), print(".", end=""), time.sleep(0.8), print(".")
                        time.sleep(0.4)
                        print("> you did it"), print("> .", end=""), time.sleep(0.8), print(".", end=""), time.sleep(
                            0.8), print(".")
                        time.sleep(0.4)
                        print("> you can go home now")
                        time.sleep(0.4)
                        print("> please, forgive yourself")
                        time.sleep(0.4)
                        print("> you can wake up now...")
                        time.sleep(0.4)
                        print("TERMINATE CONNECTION")
                        quit()
                smash_fight(try_answer)
            elif crowtaken == 'NO' and crow_deny is False:
                time.sleep(0.4)
                print("> you stand motionless in the sacristy...")
                time.sleep(0.4)
                print("> do you take the crowbar?")
                crow_deny = True
                crowbar_phase(crow_deny)
            elif crowtaken == 'NO' and crow_deny is True:
                time.sleep(0.4)
                print("> you leave the sacristy...")
                taron()
        crowbar_phase(crow_deny)
    elif sacristy_enter == 'NO':
        time.sleep(0.4)
        print("> you walk shamefully back to the front of the church, forgetful of your mission")
        game_two()

def lares():
    time.sleep(0.4)
    print("> you enter at once into a memory, one so distant yet so bitter.")
    time.sleep(0.4)
    print("> the nave is littered with discarded pews and dust, inches of dust.")
    time.sleep(0.4)
    print("> you see the two transepts, they sink away like gaping wounds, your answers lie within.")
    time.sleep(0.4)
    print("> you just want this all to be gone.")
    play_with_style()

    north_stuffs = False
    south_stuffs = False
    def lares_loop(north_stuffs, south_stuffs):
        time.sleep(0.4)
        print("> A) go to North transept")
        time.sleep(0.4)
        print("> B) go to South transept")
        time.sleep(0.4)
        print("> C) sit in the pews")
        time.sleep(0.4)
        print("> D) go to the apse")
        time.sleep(0.4)
        print("> E) go to the altar")
        time.sleep(0.4)
        print("> F) look around")
        time.sleep(0.4)
        your_lares_choice = input("> ")
        lares_choice = your_lares_choice.upper()
        if lares_choice not in ['A', 'B', 'C', 'D', 'E', 'F']:
            time.sleep(0.4)
            print("> please select one of the options")
            lares_loop(north_stuffs, south_stuffs)
        elif lares_choice == "A":
            if north_stuffs == True:
                time.sleep(0.4)
                print("> you don't want to go back there")
            else:
                time.sleep(0.4)
                print("> you enter the dark wing and walk down the echoing hall")
                time.sleep(0.4)
                print("> at the end you find a photo, it's a family")
                time.sleep(0.4)
                print("> .", end=""), time.sleep(0.8), print(".", end=""), time.sleep(0.8), print(".")
                time.sleep(0.4)
                print("> it's you! You and your...")
                time.sleep(0.4)
                print("> .", end=""), time.sleep(0.8), print(".", end=""), time.sleep(0.8), print(".")
                time.sleep(0.4)
                print("> ... your parents")
                time.sleep(0.4)
                print("> there's also a pot of oil, both of which you take.")
                north_stuffs = True
            lares_loop(north_stuffs, south_stuffs)
        elif lares_choice == "B":
            if south_stuffs == True:
                time.sleep(0.4)
                print("> you don't need to go back there")
            else:
                time.sleep(0.4)
                print("> the wing is silent and bright. A warm brightness, like the remnants of a memory.")
                time.sleep(0.4)
                print("> at the end you see a child...")
                time.sleep(0.4)
                print("> .", end=""), time.sleep(0.8), print(".", end=""), time.sleep(0.8), print(".")
                time.sleep(0.4)
                print("> it's you! You are holding a lamp and a padlock... The same one your father used...")
                time.sleep(0.4)
                print("> he used to keep you so long down there... you never got to see Mass...")
                time.sleep(0.4)
                print("> he gives you the lamp and the padlock. He knows why you are here")
                south_stuffs = True

            lares_loop(north_stuffs, south_stuffs)
        elif lares_choice == "C":
            time.sleep(0.4)
            print("> you set a pew down and sit at one end")
            time.sleep(5)
            lares_loop(north_stuffs, south_stuffs)
        elif lares_choice == "D":
            if north_stuffs is False or south_stuffs is False:
                time.sleep(0.4)
                print("> this place is still useless to you.")
                lares_loop(north_stuffs, south_stuffs)
            else:
                time.sleep(0.4)
                print("> you lay the memories together in a pile, as they were.")
                time.sleep(0.4)
                print("> you set the oil to them and drop the lamp.")
                time.sleep(0.4)
                print("> the flames rise and spread almost instantly, you feel the weight of everything leave.")
                time.sleep(0.4)
                print("> the inferno gnaws at you, and the sweet release of death takes you.")
                time.sleep(0.4)
                print("> you are forgiven, you can finally enter the house of your Father...")
                time.sleep(0.4)
                print("> you can wake up now, live in peace")
                time.sleep(0.4)
                print("TERMINATE CONNECTION")
                time.sleep(1)
                quit()
        elif lares_choice == "E":
            def hate_choice():
                time.sleep(0.4)
                print("> you must kneel, do you accept?")
                time.sleep(0.4)
                choicer = input("> ")
                choice = choicer.upper()
                if choice not in ['YES', 'NO']:
                    hate_choice()
                elif choice == "YES":
                    time.sleep(0.4)
                    print("> .", end=""), time.sleep(0.8), print(".", end=""), time.sleep(0.8), print("."), print(
                        "> then you chose to continue your torment.")
                    time.sleep(0.4)
                    print("> farewell...")
                    time.sleep(1)
                    print("TERMINATE CONNECTION")
                    time.sleep(1)
                    quit()
                else:
                    time.sleep(0.4)
                    print("> Find your freedom, then")
                    lares_loop(north_stuffs, south_stuffs)
            hate_choice()
        elif lares_choice == "F":
            time.sleep(0.4)
            print("> you take in your surroundings and make a mental image.")
            time.sleep(0.4)
            print(">                  ___________")
            time.sleep(0.4)
            print(">                 /  sacristy \\")
            time.sleep(0.4)
            print(">              __/ _ _ _ _ _ _ \\__")
            time.sleep(0.4)
            print(">             /        apse        \\")
            time.sleep(0.4)
            print(">       _____/                      \\_____")
            time.sleep(0.4)
            print(">      /            ----------             \\")
            time.sleep(0.4)
            print(">      |               altar                |")
            time.sleep(0.4)
            print(">      |North   |                  |South   |")
            time.sleep(0.4)
            print(">      |transept|                  |transept|")
            time.sleep(0.4)
            print(">      \\________|                  |________/")
            time.sleep(0.4)
            print(">               |                  |")
            time.sleep(0.4)
            print(">               |                  |")
            time.sleep(0.4)
            print(">               |      nave        |")
            time.sleep(0.4)
            print(">               |                  |")
            time.sleep(0.4)
            print(">               |                  |")
            time.sleep(0.4)
            print(">               |                  |")
            time.sleep(0.4)
            print(">               |                  |")
            time.sleep(0.4)
            print(">               | _ _ _ _ _ _ _ _ _|")
            time.sleep(0.4)
            print(">               |      narthex     |")
            time.sleep(0.4)
            print(">               \__________________/")
            time.sleep(0.4)
            print(">                      \\___/")
            # this diagram took so bloody long to draw!
            lares_loop(north_stuffs, south_stuffs)
    lares_loop(north_stuffs, south_stuffs)
def game_two():
    church_key = False
    time.sleep(0.4)
    print("> you enter the courtyart, the ground here hates you, the church hates you and you feel it.")
    time.sleep(2)
    print("> everything is dead as far as you can tell.")
    play_with_style()
    time.sleep(0.4)
    print("> A) enter the church")
    time.sleep(0.5)
    print("> B) look around")
    time.sleep(0.5)
    print("> C) go to the side of the church")
    time.sleep(0.5)
    print("> D) give up")
    def game_two_loop(church_key):
        time.sleep(0.4)
        second_choice = input("> ")
        your_second_choice = second_choice.upper()
        if your_second_choice not in ['A', 'B', 'C', 'D', 'E']:
            time.sleep(0.4)
            print('> please select one of the options')
            game_two_loop(church_key)
        elif your_second_choice == "A":
            if church_key is True:
                time.sleep(0.4)
                print("> you already knew the key would fit...")
                lares()
            else:
                time.sleep(0.4)
                print("> it's locked, you don't want you to go in")
                game_two_loop(church_key)
        elif your_second_choice == "B":
            time.sleep(0.4)
            print("> you keep your head low, you don't want to look at the courtyard more than you already have.")
            time.sleep(2)
            print("> you tap your side anxiously, and find a key. you knew it was there already.")
            church_key = True
            game_two_loop(church_key)
        elif your_second_choice == "C":
            time.sleep(0.4)
            print("> you bypass the entrance and go down the Epistle side of the church")
            time.sleep(0.4)
            print("> you come to the back of the sacristy, it's all sad, you weren't supposed to see this")
            taron()
        elif your_second_choice == "D":
            time.sleep(0.4)
            print("> there is no going back now. do what you came here to")
            game_two_loop(church_key)
    game_two_loop(church_key)

def game():
    time.sleep(0.4)
    first_choice = input("> ")
    your_first_choice = first_choice.upper()
    if your_first_choice not in ['A', 'B', 'C', 'D']:
        time.sleep(0.4)
        print('> please select one of the options')
        game()
    elif your_first_choice == 'A':
        time.sleep(0.4)
        print("> you stand at the gate of your childhood church. the trees are all dead.")
        time.sleep(0.5)
        time.sleep(0.4)
        print("> you are stronger than the trees.")
        game()
    elif your_first_choice == 'B':
        time.sleep(0.4)
        print('> there is no gate')
        game_two()
    elif your_first_choice == 'C':
        time.sleep(0.4)
        print('> the tarmac feels... comfortable')
        time.sleep(1)
        print("> you wish you were a passing cloud")
        game()
    elif your_first_choice == 'D':
        time.sleep(0.4)
        print('> it isn\'t too late... Please wake up')
        time.sleep(0.4)
        print("> please come home...")
        time.sleep(1)
        print("TERMINATE CONNECTION")
        time.sleep(0.4)
        quit()
game()
