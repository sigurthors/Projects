from game import Game

def start_game():
    g = Game()

    player = input("Enter your name: ")
    g.set_player(player)

    print("\nWelcome,", g.get_player())

    while g.update_round() > 0:
        print("\n", g.get_round(), "rounds left")
        roll_input = input("\nEnter any key to roll:")
        g.roll_dices()
        
        print("\nYou roll: ", g.get_roll())
        print("You can add score to", g.hand(), "\n")
        
        answer = ''
        rerolls = 2
        while rerolls >= 0:
            print("Write down where you want to add your roll to the score. [example: Pair]\nEnter R to re roll.\t", rerolls ,"re-rolls left")
            answer = input()
            if answer.lower() == 'r' and rerolls > 0:
                print("Write the index of the dices you want to keep ranging from 1-5")
                dices_to_keep = input()
                roll = g.reroll(dices_to_keep)
                rerolls -= 1
                print("\nYou rerolled: ", g.get_roll())
                print("You can add score to", g.hand(), "\n")
            elif answer.title() in g.hand() and g.check_if_score(answer.title()) == "":
                g.add_score(answer)
                break
            else:
                print("\nError in your input\n - Roll does not qualify for that score \n - Input misspelled\n - Combination already has a score\n - Add 0 in front of the combination name to 0 score typed\n")
        
        scorelis = g.get_score()
        for score in g.get_score().keys():
            print(score, " - ", scorelis[score])

start_game()