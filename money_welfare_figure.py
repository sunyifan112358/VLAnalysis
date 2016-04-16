import matplotlib.pyplot as plt

from figure import Figure
from color_provider import ColorProvider

class MoneyWelfareFigure(Figure):
    
    def __init__(self):
        pass
        
    def draw(self, sessions):
        
        money_avg, welfare_avg = self.get_mean(sessions)
        print money_avg

        for session in sessions:
            money = []
            welfare = []
            
            money.append(session.challenge[0].money - money_avg[0])
            money.append(session.challenge[1].money - money_avg[1])
            money.append(session.challenge[2].money - money_avg[2])

            welfare.append(session.challenge[0].welfare - welfare_avg[0])
            welfare.append(session.challenge[1].welfare - welfare_avg[1])
            welfare.append(session.challenge[2].welfare - welfare_avg[2])

            line_style = 'k-'
            if not session.give_recommendation():
                line_style = 'k--'
            plt.plot(welfare, money, line_style, linewidth = 0.2)

            color = ColorProvider.r[
                (session.cluster_tags['money_welfare_0'] -1)]
            plt.plot(welfare[0], money[0], 'D', color = color, markersize = 12)

            color = ColorProvider.g[
                (session.cluster_tags['money_welfare_1'] - 1)]
            plt.plot(welfare[1], money[1], 'o', color = color, markersize = 12)

            color = ColorProvider.b[
                (session.cluster_tags['money_welfare_2'] - 1)]
            plt.plot(welfare[2], money[2], '^', color = color, markersize = 12)

        self.set_x_label("Welfare")
        self.set_y_label("Earnings")
#plt.xlim((-0.5, 3.5))

    def get_mean(self, sessions):
        money = [[], [], []]
        welfare = [[], [], []]

        money_avg = [0, 0, 0]
        welfare_avg = [0, 0, 0]

        for session in sessions:
            for i in range(len(session.challenge)):
                money[i].append(session.challenge[i].money)
                welfare[i].append(session.challenge[i].welfare)

        for i in range(len(money)):
            money_avg[i] = sum(money[i])/len(money[i])
            welfare_avg[i] = sum(welfare[i])/len(welfare[i])

        return money_avg, welfare_avg

