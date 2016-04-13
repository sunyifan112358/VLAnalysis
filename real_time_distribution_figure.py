import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class RealTimeDistributionFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        real_time = [[], [], []]
        for session in sessions:
            real_time[0].append(session.challenge1.get_real_duration())
            real_time[1].append(session.challenge2.get_real_duration())
            real_time[2].append(session.challenge3.get_real_duration())

        plt.boxplot(real_time, showmeans=True)

        self.set_x_label("Challenge")
        self.set_y_label("real_time")
