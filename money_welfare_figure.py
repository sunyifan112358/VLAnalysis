import matplotlib.pyplot as plt

from figure import Figure
from color_provider import ColorProvider

class MoneyWelfareFigure(Figure):
    
    def __init__(self):
        pass

    def set_challenge_number(self, challenge_number):
        self.challenge_number = challenge_number
        
    def draw(self, sessions, global_stat):
        
        for session in sessions:
            money = []
            welfare = []

            color_provider = ColorProvider()
            for i in self.challenge_number:
                if len(session.challenge) <= i:
                    continue
                challenge = session.challenge[i]
    
                money_avg, welfare_avg = global_stat.get_mean(i, 
                        challenge.get_oil_cleaning_solution())

                money.append(challenge.money)
                welfare.append(challenge.welfare)

                color_list = color_provider.get_color_list(i)
                cluster_tag_name = '_money_welfare_' + str(i)
                cluster_tag = session.cluster_tags[cluster_tag_name]
                color = color_list[(cluster_tag - 1) * 2]
                plt.plot(welfare[-1], money[-1], self.get_marker_shape(i),
                        color = color, markersize = 12)

                plt.annotate(session.name, xy=(welfare[-1], money[-1]))
               
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
