import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class MoneyDistributionFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        money = [[], [], []]
        for session in sessions:
            money[0].append(session.challenge[0].money)
            money[1].append(session.challenge[1].money)
            money[2].append(session.challenge[2].money)

        plt.boxplot(money, showmeans=True)

        self.set_x_label("Challenge")
        self.set_y_label("Earnings")
