import re
from collections import Counter as count
from random import uniform as roll

class Game:
    def __init__(self):
        self.player = 1
        self.score = {"1": "" ,"2": "", "3": "", "4": "", "5": "", "6": "", "Pair": "", "Two Pairs": "", "Three Of A Kind": "", "Four Of A Kind": "", "Small Straight": "", "Large Straight": "", "Full House": "", "Yatzy": "", "Chance": ""}
        self.score2 = {"1": "" ,"2": "", "3": "", "4": "", "5": "", "6": "", "Pair": "", "Two Pairs": "", "Three Of A Kind": "", "Four Of A Kind": "", "Small Straight": "", "Large Straight": "", "Full House": "", "Yatzy": "", "Chance": ""}
        self.round = 30
        self.roll = []
        self.rerolls = 2

    def set_player(self, pname):
        self.player = pname

    def get_player(self):
        return self.player

    def get_score(self):
        return self.score

    def get_score2(self):
        return self.score2

    def check_if_score(self, key):
        if self.player == 1:
            return self.score[key.title()]
        elif self.player == 2:
            return self.score2[key.title()]
    
    def get_rerolls(self):
        return self.rerolls

    def get_roll(self):
        return self.roll

    def get_round(self):
        return self.round

    def get_winner(self):
        player1_total = 0
        for num in self.score.values():
            if num != "":
                player1_total += num

        player2_total = 0
        for num in self.score2.values():
            if num != "":
                player2_total += num

        if player1_total > player2_total:
            return 1
        else:
            return 2

    def reset_rerolls(self):
        self.rerolls = 2
    
    def update_round(self):
        self.round -= 1
        return self.round

    def update_player(self):
        if self.player == 1:
            self.player = 2
        elif self.player == 2:
            self.player = 1

    def roll_dices(self):
        self.roll = sorted([int(roll(1,7)) for i in range(1,6)])
        return self.roll

    def reroll(self, kept):
        kept = re.sub(' ', '', kept)
        kept = re.sub(',', '', kept)
        for dice in kept:
            self.roll[int(dice)-1] = int(roll(1,7))
        self.roll = sorted(self.roll)
        self.rerolls -= 1
        return self.roll

    def hand(self):
        player_roll = self.roll
        most_common = count(self.roll).most_common(5) #Checks for dices that are the same
        possible_score = []

        if set(player_roll) == 1  and self.check_if_score("Yatzy") == "":
            possible_score.append("Yatzy")
        else:
            if player_roll == [2, 3, 4, 5, 6] and self.check_if_score("Large Straight") == "":
                hand_score = "Large Straight"
                possible_score.append(hand_score)
            if player_roll == [1, 2, 3, 4, 5] and self.check_if_score("Small Straight") == "":
                hand_score = "Small Straight"
                possible_score.append(hand_score)
            if most_common[0][1] == 3 and most_common[1][1] == 2  and self.check_if_score("Full House") == "":
                hand_score = "Full House"
                possible_score.append(hand_score)
            if most_common[0][1] == 4 and self.check_if_score("Four Of A Kind") == "":
                hand_score = "Four Of A Kind"
                possible_score.append(hand_score)
            if most_common[0][1] == 3 and self.check_if_score("Three Of A Kind") == "":
                hand_score = "Three Of A Kind"
                possible_score.append(hand_score)
            if most_common[0][1] == 2 and most_common[1][1] == 2  and self.check_if_score("Two Pairs") == "":
                hand_score = "Two Pairs"
                possible_score.append(hand_score)
            if most_common[0][1] == 2 and self.check_if_score("Pair") == "":
                hand_score = "Pair"
                possible_score.append(hand_score)
            if 6 in player_roll and self.check_if_score("6") == "":
                hand_score = "6"
                possible_score.append(hand_score)
            if 5 in player_roll and self.check_if_score("5") == "":
                hand_score = "5"
                possible_score.append(hand_score)
            if 4 in player_roll and self.check_if_score("4") == "":
                hand_score = "4"
                possible_score.append(hand_score)
            if 3 in player_roll and self.check_if_score("3") == "":
                hand_score = "3"
                possible_score.append(hand_score)
            if 2 in player_roll and self.check_if_score("2") == "":
                hand_score = "2"
                possible_score.append(hand_score)
            if 1 in player_roll and self.check_if_score("1") == "":
                hand_score = "1"
                possible_score.append(hand_score)
            if  self.check_if_score("Chance") == "":
                possible_score.append("Chance")
        return possible_score

    def add_score(self, comb):
            comb = comb.title()
            most_common = count(self.roll).most_common(5)

            if comb not in self.hand():
                if self.player == 1:
                    if self.score[comb] == "":
                        self.score[comb] = 0
                else:
                    if self.score2[comb] == "":
                        self.score2[comb] = 0
            else:
                if comb == "Yatzy":
                    if self.player == 1:
                        self.score[comb] = 50
                    else:
                        self.score2[comb] = 50
                elif comb == "Large Straight":
                    if self.player == 1:
                        self.score[comb] = 40
                    else:
                        self.score2[comb] = 40
                elif comb == "Small Straight":
                    if self.player == 1:
                        self.score[comb] = 30
                    else:
                        self.score2[comb] = 30
                elif comb == "Full House":
                    points = most_common[0][0] * most_common[0][1]
                    points2 = most_common[1][0] * most_common[1][1]
                    if self.player == 1:
                        self.score[comb] = points + points2
                    else:
                        self.score2[comb] = points + points2
                elif comb == "Four Of A Kind":
                    points = most_common[0][0] * most_common[0][1]
                    if self.player == 1:
                        self.score[comb] = points
                    else:
                        self.score2[comb] = points
                elif comb == "Three Of A Kind":
                    points = most_common[0][0] * most_common[0][1]
                    if self.player == 1:
                        self.score[comb] = points
                    else:
                        self.score2[comb] = points
                elif comb == "Two Pairs":
                    points = most_common[0][0] * most_common[0][1]
                    points2 = most_common[1][0] * most_common[1][1]
                    if self.player == 1:
                        self.score[comb] = points + points2
                    else:
                        self.score2[comb] = points + points2
                elif comb == "Pair":
                    points = most_common[0][0] * most_common[0][1]
                    if self.player == 1:
                        self.score[comb] = points
                    else:
                        self.score2[comb] = points
                elif comb == "6":
                    points = [x for x in self.roll if x == 6]
                    if self.player == 1:
                        self.score[comb] = sum(points)
                    else:
                        self.score2[comb] = sum(points)
                elif comb == "5":
                    points = [x for x in self.roll if x == 5]
                    if self.player == 1:
                        self.score[comb] = sum(points)
                    else:
                        self.score2[comb] = sum(points)
                elif comb == "4":
                    points = [x for x in self.roll if x == 4]
                    if self.player == 1:
                        self.score[comb] = sum(points)
                    else:
                        self.score2[comb] = sum(points)
                elif comb == "3":
                    points = [x for x in self.roll if x == 3]
                    if self.player == 1:
                        self.score[comb] = sum(points)
                    else:
                        self.score2[comb] = sum(points)
                elif comb == "2":
                    points = [x for x in self.roll if x == 2]
                    if self.player == 1:
                        self.score[comb] = sum(points)
                    else:
                        self.score2[comb] = sum(points)
                elif comb == "1":
                    points = [x for x in self.roll if x == 1]
                    if self.player == 1:
                        self.score[comb] = sum(points)
                    else:
                        self.score2[comb] = sum(points)
                elif comb == "Chance" and self.check_if_score("Chance") == "":
                    if self.player == 1:
                        self.score[comb] = sum(self.roll)
                    else:
                        self.score2[comb] = sum(self.roll)

