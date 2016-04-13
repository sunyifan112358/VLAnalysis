import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class WelfareScatterFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        for session in sessions:
            welfare = []
            welfare.append(session.challenge1.welfare)
            welfare.append(session.challenge2.welfare)
            welfare.append(session.challenge3.welfare)
            plt.plot(welfare, "-ko", linewidth = 0.2)

        self.set_x_label("Challenge")
        self.set_y_label("Earnings")