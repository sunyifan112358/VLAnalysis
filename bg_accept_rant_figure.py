import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class BgAcceptanceRateFigure(Figure):

    def __init__(self):
        pass

    def draw(self, sessions):
        accept = [[], [], [], [], [], [], [], [], []]
        for session in sessions:

            if not session.give_recommendation():
                continue

            offset = 0
            if session.bg_tag == 'STEM':
                offset = 1
            elif session.bg_tag == "non-STEM":
                offset = 2
            
            for i in range(1, len(session.challenge)):
                rate = session.challenge[i].get_recommendation_acceptance_rate()
                accept[(i - 1) * 3 + offset].append(rate)


        plt.boxplot(accept, showmeans=True)
        plt.xticks(range(1, 10), 
            ['C2-CSCE', 'C2-STEM', 'C2-non-STEM', 
            'C3-CSCE', 'C3-STEM', 'C3-non-STEM'], 
            rotation = 60)

        self.set_x_label("Challenge")
        self.set_y_label("Acceptance Rate")
