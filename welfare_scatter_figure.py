import matplotlib.pyplot as plt
import numpy as np

from figure import Figure
from color_provider import ColorProvider

class WelfareScatterFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        for session in sessions:
            if not session.finished_all_challenges():
                continue

            welfare = []
            welfare.append(session.challenge[0].welfare)
            welfare.append(session.challenge[1].welfare)
            welfare.append(session.challenge[2].welfare)

            color_provider = ColorProvider()
            color = color_provider[
                session.cluster_tags['_welfare_0_1_2'] - 1]
            plt.plot([1, 2, 3], welfare, "-o", linewidth = 0.2, color = color)

        self.set_x_label("Challenge")
        self.set_y_label("Welfare")
        plt.xlim((0.8, 3.2))
        plt.xticks([1, 2, 3], ['1', '2', '3'])
