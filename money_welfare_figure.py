import matplotlib.pyplot as plt

from figure import Figure
from color_provider import ColorProvider

class MoneyWelfareFigure(Figure):
    
    def __init__(self):
        pass
        
    def draw(self, sessions):
        for session in sessions:
            money = []
            welfare = []
            
            money.append(session.challenge[0].money)
            money.append(session.challenge[1].money)
            money.append(session.challenge[2].money)

            welfare.append(session.challenge[0].welfare)
            welfare.append(session.challenge[1].welfare)
            welfare.append(session.challenge[2].welfare)

            line_style = 'k-'
            if not session.give_recommendation():
                line_style = 'k--'
            plt.plot(welfare, money, line_style, linewidth = 0.2)

            color = ColorProvider.r[(session.cluster_tags['money_welfare_0'] - 1) * 4]
            plt.plot(welfare[0], money[0], 'D', color = color, markersize = 12)

            color = ColorProvider.g[(session.cluster_tags['money_welfare_1'] - 1) * 4]
            plt.plot(welfare[1], money[1], 'o', color = color, markersize = 12)

            color = ColorProvider.b[(session.cluster_tags['money_welfare_2'] - 1) * 4]
            plt.plot(welfare[2], money[2], '^', color = color, markersize = 12)

        self.set_x_label("Welfare")
        self.set_y_label("Earnings")
        plt.xlim((-0.5, 3.5))
            

