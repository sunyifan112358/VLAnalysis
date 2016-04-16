import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class MoneyDistributionFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        money = [[], [], [], [], []]
        for session in sessions:
            money[0].append(session.challenge[0].money)
            if session.give_recommendation():
                money[1].append(session.challenge[1].money)
                money[3].append(session.challenge[2].money)
            else:
                money[2].append(session.challenge[1].money)
                money[4].append(session.challenge[2].money)


        plt.boxplot(money, showmeans=True)
        plt.xticks(range(1, 6), ['C1', 'C2-Rec', 'C2-NoRec', 'C3-Rec', 'C3-NoRec'])

        self.set_x_label("Challenge")
        self.set_y_label("Earnings")
