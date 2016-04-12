import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class MoneyScatterFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        for session in sessions:
            money = []
            money.append(session.challenge1.money)
            money.append(session.challenge2.money)
            money.append(session.challenge3.money)
            plt.plot(money, "-ko", linewidth = 0.2)

        self.set_x_label("Challenge")
        self.set_y_label("Earnings")
