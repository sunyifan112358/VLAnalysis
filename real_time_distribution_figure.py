import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class RealTimeDistributionFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        real_time = [[], [], []]
        for session in sessions:
            for i in range(len(session.challenge)):
                real_time[i].append(session.challenge[i].get_real_duration())

        plt.boxplot(real_time, showmeans=True)

        self.set_x_label("Challenge")
        self.set_y_label("real_time")
