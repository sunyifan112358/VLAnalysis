import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class WelfareDistributionFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        welfare = [[], [], []]
        for session in sessions:
            welfare[0].append(session.challenge1.welfare)
            welfare[1].append(session.challenge2.welfare)
            welfare[2].append(session.challenge3.welfare)

        plt.boxplot(welfare, showmeans=True)

        self.set_x_label("Challenge")
        self.set_y_label("Welfare")
