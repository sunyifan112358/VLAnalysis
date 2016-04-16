import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class WelfareScatterFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        for session in sessions:
            welfare = []
            welfare.append(session.challenge[0].welfare)
            welfare.append(session.challenge[1].welfare)
            welfare.append(session.challenge[2].welfare)
            plt.plot([1, 2, 3], welfare, "-ko", linewidth = 0.2)

        self.set_x_label("Challenge")
        self.set_y_label("Welfare")
