import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class MoneyScatterFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        for session in sessions:
            money = []
            money.append(session.challenge[0].money)
            money.append(session.challenge[1].money)
            money.append(session.challenge[2].money)
            plt.plot([1, 2, 3], money, "-ko", linewidth = 0.2)

        self.set_x_label("Challenge")
        self.set_y_label("Earnings")
