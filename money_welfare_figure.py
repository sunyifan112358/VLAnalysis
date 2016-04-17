import matplotlib.pyplot as plt

from figure import Figure
from color_provider import ColorProvider

class MoneyWelfareFigure(Figure):
    
    def __init__(self):
        pass
        
    def draw(self, sessions):
        
        money_avg, welfare_avg = self.get_mean(sessions)

        for session in sessions:
            money = []
            welfare = []

            color_provider = ColorProvider()
            for i in range(len(session.challenge)):
                challenge = session.challenge[i]
                money.append(challenge.money)
                welfare.append(challenge.welfare)

                color_list = color_provider.get_color_list(i)
                cluster_tag_name = '_money_welfare_' + str(i)
                cluster_tag = session.cluster_tags[cluster_tag_name]
                color = color_list[(cluster_tag - 1) * 2]
                plt.plot(welfare[i], money[i], self.get_marker_shape(i),
                        color = color, markersize = 12)
               
            line_style = 'k-'
            if not session.give_recommendation():
                line_style = 'k--'
            plt.plot(welfare, money, line_style, linewidth = 0.2)
        


        self.set_x_label("Welfare")
        self.set_y_label("Earnings")
#plt.xlim((-0.1, 3.1))
#plt.ylim((-0.4e7, 0.7e7))

    def get_marker_shape(self, index):
        if index == 0:
            return 'D'
        elif index == 1:
            return 'o'
        else:
            return '^'

    def get_mean(self, sessions):
        money = [[], [], []]
        welfare = [[], [], []]

        money_avg = [0, 0, 0]
        welfare_avg = [0, 0, 0]

        for session in sessions:
            for i in range(len(session.challenge)):
                challenge = session.challenge[i]
                if challenge == None:
                    continue
                money[i].append(challenge.money)
                welfare[i].append(challenge.welfare)

        for i in range(len(money)):
            money_avg[i] = sum(money[i])/len(money[i])
            welfare_avg[i] = sum(welfare[i])/len(welfare[i])

        return money_avg, welfare_avg

