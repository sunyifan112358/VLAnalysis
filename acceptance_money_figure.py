from scipy.stats import linregress
import matplotlib.pyplot as plt
import numpy as np

from figure import Figure
from decision_phase_acceptance_figure import DecisionPhaseAcceptanceFigure

class AcceptanceMoneyFigure(Figure):

    def __init__(self):
        self.skip_challenge1_win = False
        self.skip_challenge1_lose = False
        self.use_welfare = False

    def SkipChallenge1Win(self):
        self.skip_challenge1_win = True

    def SkipChallenge1Lose(self):
        self.skip_challenge1_lose = True

    def UseWelfare(self):
        self.use_welfare = True

    def draw(self, sessions):

        c2_acceptance = []
        c2_money = []
        c3_acceptance = []
        c3_money = []

        data_extractor = DecisionPhaseAcceptanceFigure()

        for session in sessions:
            if not session.finished_all_challenges():
                continue

            if not session.give_recommendation():
                continue

            if self.skip_challenge1_win:
                if session.is_win(0):
                    continue

            if self.skip_challenge1_lose:
                if not session.is_win(0):
                    continue


            if session.challenge[1].get_oil_cleaning_solution() == "None" \
                or session.challenge[1].get_oil_cleaning_solution() == "Skimmers":
                continue

            if session.challenge[2].get_oil_cleaning_solution() == "None" \
                or session.challenge[2].get_oil_cleaning_solution() == "Skimmers":
                continue
            

            c1 = session.challenge[0]
            c2 = session.challenge[1]
            c2_accept, c2_deny = data_extractor.get_challenge_data(c2)
            c2_acc_rate = 0
            if sum(c2_accept) + sum(c2_deny) != 0:
                c2_acc_rate = 1.0 * sum(c2_accept) / \
                    (sum(c2_accept) + sum(c2_deny))

            c3 = session.challenge[2]
            c3_accept, c3_deny = data_extractor.get_challenge_data(c3)
            c3_acc_rate = 0
            if sum(c3_accept) + sum(c3_deny) != 0:
                c3_acc_rate = 1.0 * sum(c3_accept) / \
                    (sum(c3_accept) + sum(c3_deny))


            acceptance_rate = [
                c2_acc_rate,
                c3_acc_rate,
            ]

            if self.use_welfare:
                money = [c2.welfare, c3.welfare]
            else:
                money = [c2.money, c3.money]


            c2_acceptance.append(c2_acc_rate)
            c3_acceptance.append(c2_acc_rate)
            if self.use_welfare:
                c2_money.append(c2.welfare)
                c3_money.append(c3.welfare)
            else:
                c2_money.append(c2.money)
                c3_money.append(c3.money)


            plt.plot(acceptance_rate, money, 'k-', linewidth = 0.2)
            plt.plot(acceptance_rate[0], money[0], 'go')
            plt.plot(acceptance_rate[1], money[1], 'b^')


        slope, intercept, r_value, p_value, std_err = \
                linregress(c2_acceptance, c2_money)
        X = np.array(c2_acceptance)
        plt.plot(X, slope * X + intercept, 'g',
                linewidth = 0.2)

        slope, intercept, r_value, p_value, std_err = \
                linregress(c3_acceptance, c3_money)
        X = np.array(c3_acceptance)
        plt.plot(X, slope * X + intercept, 'b',
                linewidth = 0.2)



        self.set_x_label("Acceptance Rate")

        if self.use_welfare:
            self.set_y_label("Welfare")
        else:
            self.set_y_label("Earnings")
