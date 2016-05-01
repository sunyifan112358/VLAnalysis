import matplotlib.pyplot as plt
import matplotlib
import numpy as np

from figure import Figure

class SolutionScatterFigure(Figure):

    def __init__(self):
        super(SolutionScatterFigure, self).__init__();

    def draw(self, sessions):

        win_change_count = 0
        win_stay_count = 0
        lose_change_count = 0
        lose_stay_count = 0

        for session in sessions:
            if not session.finished_all_challenges():
                continue

            c1_solution = session.challenge[0].get_oil_cleaning_solution()
            c2_solution = session.challenge[1].get_oil_cleaning_solution()
            c3_solution = session.challenge[2].get_oil_cleaning_solution()
            c1_win = session.is_win(0)
            c2_win = session.is_win(1)
            c3_win = session.is_win(2)

            if c2_solution != c1_solution:
                if c1_win:
                    win_change_count += 1
                else:
                    lose_change_count += 1
            else:
                if c1_win:
                    win_stay_count += 1
                else:
                    lose_stay_count += 1

            if c3_solution != c2_solution:
                if c2_win:
                    win_change_count += 1
                else:
                    lose_change_count += 1
            else:
                if c2_win:
                    win_stay_count += 1
                else:
                    lose_stay_count += 1



            self.plot_challenge(session, 0)
            self.plot_challenge(session, 1)
            self.plot_challenge(session, 2)

        plt.scatter(-1, -1, 48, marker = 's',
            color = "#ffffff", edgecolors = "black",
            label="None")
        plt.scatter(-1, -1, 48, marker = 'D',
            color = "#ffffff", edgecolors = "black",
            label="Burn")
        plt.scatter(-1, -1, 48, marker = 'o',
            color = "#ffffff", edgecolors = "black",
            label="Disp")
        plt.scatter(-1, -1, 48, marker = '^',
            color = "#ffffff", edgecolors = "black",
            label="Skmr")
        plt.scatter(-1, -1, 48, marker = 'o',
            color = "green", edgecolors = "black",
            label="Win")
        plt.scatter(-1, -1, 48, marker = 'o',
            color = "red", edgecolors = "black",
            label="Lose")
        plt.scatter(-1, -1, s = 48, marker = 's',
            color = "#ffffff", edgecolors = "black",
            label="w/ Rec")
        plt.scatter(-1, -1, s = 48, marker = 's',
            color = "#ffffff", edgecolors = "black",
            hatch = "////",
            label="w/o Rec")

        self.ax.set_ylim(0.7, 4.2)
        self.ax.set_xlim(0, 41)
        self.set_x_label('Players')
        self.set_y_label('Challenges')

        plt.legend(loc="upper center", ncol=3,
            numpoints = 1, scatterpoints = 1,
            fontsize = self.font_size,
            labelspacing = 0,
            columnspacing = 0)

        self.ax.set_yticks([1, 2, 3])
        self.ax.set_yticklabels(['1', '2', '3'])

        self.ax.set_xticks(np.arange(41), minor=True)
        self.ax.xaxis.grid(which='minor')

        print("Win change",  win_change_count)
        print("Win stay",  win_stay_count)
        print("Lose change",  lose_change_count)
        print("Lose stay",  lose_stay_count)


    def plot_challenge(self, session, challenge_number):
        challenge = session.challenge[challenge_number]
        solution = challenge.get_oil_cleaning_solution()
        symbol = self.get_cleaning_symbol(solution)

        is_win = session.is_win(challenge_number)
        color = self.get_win_lose_color(is_win)

        win_word = 'lose'
        if is_win:
            win_word = 'win'

        hatch = ""
        if not session.give_recommendation():
            hatch = "//////"

        plt.scatter(session.id, challenge_number + 1,
                s = 48,
                marker = symbol, c = color,
                hatch = hatch)

    def get_cleaning_symbol(self, solution):
        if solution == "None":
            return 's'
        elif solution == "Burn":
            return 'D'
        elif solution == "Dispersant":
            return 'o'
        elif solution == "Skimmers":
            return '^'
        else:
            print(solution)

    def get_win_lose_color(self, is_win):
        if is_win:
            return 'g'
        else:
            return 'r'
