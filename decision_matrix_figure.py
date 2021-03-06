import matplotlib.pyplot as plt
import matplotlib
import numpy as np

from figure import Figure
from decision_matrix import DecisionMatrix
from phase_action import PhaseAction

class DecisionMatrixFigure(Figure):

    def __init__(self):
        pass

    def draw(self, session, challenge):
        decision_matrix_extractor = DecisionMatrix()
        decision_matrix = decision_matrix_extractor.extract_decision_matrix(challenge)

        data = np.array(decision_matrix)

        priority_value = np.array(decision_matrix)
        for p in np.nditer(priority_value, op_flags=['readwrite']):
            if p != 0:
                p[...] = 1.0 / p
        self.dump_csv(session, priority_value)

        # color_map = matplotlib.colors.LinearSegmentedColormap.from_list(
        #        'custom', ['r', '#eeeeee'], N = 256)
        color_map = matplotlib.colors.ListedColormap(
        ['#cc0000',
        '#ff9933', '#ff9933',
        '#ccff33', '#ccff33', '#ccff33', '#ccff33', '#ccff33',
        '#009933', '#009933', '#009933', '#009933', '#009933', '#009933', '#009933', '#009933', '#009933', '#009933', '#009933', '#009933', ], 'custom', 20)
        color_map.set_under(color = 'w')


        plt.pcolor(priority_value, cmap = color_map, vmin = 1, vmax = 20)
        cb = plt.colorbar(pad = 0.19)
        cb.ax.invert_yaxis()

        self.money, self.welfare = self.extract_money_welfare_data(challenge)
        self.plot_money()
        self.plot_welfare()

        self.ax.invert_yaxis()
        self.ax.xaxis.grid(which='minor')
        self.ax.yaxis.grid(which='minor')

        self.ax.set_xticks(np.arange(19) + 0.5)
        self.ax.set_xticklabels(np.arange(19) + 1)
        self.ax.set_xticks(np.arange(20), minor=True)
        self.ax.set_yticks(np.arange(30) + 0.5)
        self.ax.set_yticklabels(np.arange(30) + 1)
        self.ax.set_yticks(np.arange(30), minor=True)

        self.set_x_label("Decision Phase")
        self.set_y_label("Ship ID")

        h1, l1 = self.ax2.get_legend_handles_labels()
        h2, l2 = self.ax3.get_legend_handles_labels()
        plt.legend(h1+h2, l1+l2, loc="lower right")

    def dump_csv(self, session, decision_matrix):
        np.savetxt(session.name + "_decision.csv", decision_matrix,
                delimiter=", ")

    def extract_money_welfare_data(self, challenge):
        money = []
        welfare = []
        in_decision = False
        for action in challenge.actions:
            if isinstance(action, PhaseAction) and action.phase == "Decision":
                in_decision = True
                money.append(action.money)
                welfare.append(action.welfare)
            elif isinstance(action, PhaseAction) and \
                    action.phase == "Simulation" and \
                    in_decision == True:
                in_decision = False

        return money, welfare

    def plot_money(self):
        self.ax2 = self.ax.twinx()
        self.ax2.plot(np.arange(len(self.money)), self.money, '-o',
                label="Earnings", color="#0000ff")
        self.ax2.set_ylim(-6000000, 3000000)
        self.ax2.set_ylabel("Earnings")
        self.ax2.set_yticks(range(-6000000, 3000000, 1000000))
        self.ax2.set_yticklabels(['-6M', '-5M', '-4M', '-3M', '-2M',
            '-1M', '0', '1M', '2M'])

    def plot_welfare(self):
        self.ax3 = self.ax.twinx()
        self.ax3.plot(np.arange(len(self.welfare)), self.welfare, 'c-^',
                label="Welfare")
        self.ax3.set_ylim(0, 5)
        self.ax3.spines['right'].set_position(('axes', 1.15))
        self.ax3.set_ylabel("Welfare")
