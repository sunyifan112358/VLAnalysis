import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class WelfareDistributionFigure(Figure):

    def __init__(self):
        pass

    def draw(self, sessions):
        welfare = [[], [], [], [], []]
        for session in sessions:
            welfare[0].append(session.challenge[0].welfare)

            if session.give_recommendation():
                welfare[1].append(session.challenge[1].welfare)
                welfare[3].append(session.challenge[2].welfare)
            else:
                welfare[2].append(session.challenge[1].welfare)
                welfare[4].append(session.challenge[2].welfare)

        plt.boxplot(welfare, showmeans=True)
        plt.xticks(range(1, 6), ['C1', 'C2-Rec', 'C2-NoRec', 'C3-Rec', 'C3-NoRec'])

        self.set_x_label("Challenge")
        self.set_y_label("Welfare")
