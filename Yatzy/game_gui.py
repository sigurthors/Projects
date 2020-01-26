from tkinter import *
from game import Game

game = Game()

#FUNCTIONS
def roll_dice():
    if roll_button["text"] == "ROLL":
        roll = game.roll_dices()
        tmp = "Player " + str(game.get_player()) + " rolled: " + str(roll) + " " + str(game.get_rerolls()) + " re-roll left"
        curr_roll.set(tmp)
        roll_button["text"] = "REROLL"
    elif roll_button["text"] == "REROLL":
        roll = game.reroll("1")
        tmp = "Player " + str(game.get_player()) + " re-rolled: " + str(roll) + " " + str(game.get_rerolls()) + " re-roll left"
        curr_roll.set(tmp)

    if game.get_rerolls() == 0:
        roll_button.pack_forget()

    show_hand()

def show_hand():
    tmp = " - "
    for comb in game.hand():
        tmp += comb + " - "
    curr_comb.set(tmp)
    entry_comb.pack()
    btn_addScore.pack()

def add_score():
    tmpEntry = entry_comb.get()
    if game.check_if_score(tmpEntry) == "":
        game.add_score(tmpEntry)
        game.update_player()
        curr_roll.set("Player " + str(game.get_player()))
        curr_comb.set("")
        entry_comb.delete(0, 'end')
        entry_comb.pack_forget()
        btn_addScore.pack_forget()

        roll_button["text"] = "ROLL"
        roll_button.pack()

        game.reset_rerolls()
        update_round()
        update_scoreboard()

def update_scoreboard():
    tmpScore = game.get_score()
    player1_score = ""
    for key in tmpScore.keys():
        player1_score += key + " - " + str(tmpScore[key]) + "\n"
    curr_scoreboard.set(player1_score)

    tmpScore2 = game.get_score2()
    player2_score = ""
    for key in tmpScore.keys():
        player2_score += str(tmpScore2[key]) + " - " + key + "\n"
    curr_scoreboard2.set(player2_score)

def update_round():
    game.update_round()
    if game.get_round() == 0:
        display_comb.pack_forget()
        roll_button.pack_forget()

        winner = "Player " + str(game.get_winner()) + " wins!"
        curr_roll.set(winner)
        your_roll.pack()

#CANVAS
window = Tk()
window.title("Yatzy Madness")
window.configure(background="white")
Frame(width=450).pack()

#GAME TITLE
game_name = Label (window, text="Yatzy Madness")
game_name.grid(row=0, column=0)
game_name.pack(fill=X)

#YOUR ROLL
curr_roll = StringVar()
your_roll = Label (window, textvariable=curr_roll)
your_roll.grid(row=2, column=0)
your_roll.place(anchor="center")
your_roll.pack()

#COMBINATIONS FROM ROLL
curr_comb = StringVar()
display_comb = Label (window, textvariable=curr_comb)
display_comb.grid(row=4, column=0)
display_comb.place(anchor="center")
display_comb.pack()

#ROLL BUTTON
roll_button = Button(window, text="ROLL", width=18, command=roll_dice)
roll_button.grid(row=3, column=0)
roll_button.pack()

#ENTRY AND BUTTON FOR COMBINATION PICKING
entry_comb = Entry(window, justify='center')
entry_comb.grid(row=5)
entry_comb.pack()
entry_comb.pack_forget()

btn_addScore = Button(window, text="Add Score", width=18, command=add_score)
btn_addScore.grid(row=5)
btn_addScore.pack()
btn_addScore.pack_forget()

#SCOREBOARD
    #PLAYER 1
curr_scoreboard = StringVar()
scoreboard = Label(window, textvariable=curr_scoreboard, justify=LEFT)
scoreboard.grid(row=6, column=0)
scoreboard.pack(side=LEFT)

    #PLAYER 2
curr_scoreboard2 = StringVar()
scoreboard2 = Label(window, textvariable=curr_scoreboard2, justify=RIGHT)
scoreboard2.grid(row=6, column=1)
scoreboard2.pack(side=RIGHT)

update_scoreboard()


window.mainloop()