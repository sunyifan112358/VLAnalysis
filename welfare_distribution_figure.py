import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class WelfareDistributionFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        welfare = [[], [], []]
        for session in sessions:
            welfare[0].append(session.challenge[0].welfare)
            welfare[1].append(session.challenge[1].welfare)
            welfare[2].append(session.challenge[2].welfare)

        plt.boxplot(welfare, showmeans=True)

        self.set_x_label("Challenge")
        self.set_y_label("Welfare")
