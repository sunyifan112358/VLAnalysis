from scipy.stats import linregress
import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class SolutionWelfareFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        self.sessions = sessions

        self.data = [[], [], [], [], [], [], [], [], [], [], [], []]
        self.collect_data()

        plt.boxplot(self.data, showmeans = True)

        plt.xticks(range(1, 13), 
                ['C1-None', 'C1-Burning', 'C1-Dispersant', 'C1-Skimmers',
                'C2-None', 'C2-Burning', 'C2-Dispersant', 'C2-Skimmers',
                'C3-None', 'C3-Burning', 'C3-Dispersant', 'C3-Skimmers'],
                rotation=60)

        self.set_x_label("Challenges and Solutions")
        self.set_y_label("Welfare")
        

        
    def collect_data(self):
        for session in self.sessions:
            for i in range(len(session.challenge)):
                self.process_challenge(session.challenge[i], i)

    def process_challenge(self, challenge, challenge_number):
        if challenge.get_oil_cleaning_solution() == "None":
            self.data[challenge_number * 4 + 0].append(challenge.welfare)
        if challenge.get_oil_cleaning_solution() == "Burn":
            self.data[challenge_number * 4 + 1].append(challenge.welfare)
        if challenge.get_oil_cleaning_solution() == "Dispersant":
            self.data[challenge_number * 4 + 2].append(challenge.welfare)
        if challenge.get_oil_cleaning_solution() == "Skimmers":
            self.data[challenge_number * 4 + 3].append(challenge.welfare)
            


 
