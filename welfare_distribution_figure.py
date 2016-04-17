import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class WelfareDistributionFigure(Figure):

    def __init__(self):
        pass

    def draw(self, sessions):
        welfare = [[], [], [], [], [], []]
        for session in sessions:
            if session.give_recommendation():
                for i in range(len(session.challenge)):
                    welfare[i * 2].append(session.challenge[i].welfare)
            else:
                for i in range(len(session.challenge)):
                    welfare[i * 2 + 1].append(session.challenge[i].welfare)

        plt.boxplot(welfare, showmeans=True)
        plt.xticks(range(1, 7), ['C1-Rec', 'C2-NoRec', 'C2-Rec', 'C2-NoRec', 'C3-Rec', 'C3-NoRec'])

        self.set_x_label("Challenge")
        self.set_y_label("Welfare")
