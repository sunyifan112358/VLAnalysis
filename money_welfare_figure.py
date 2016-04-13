import matplotlib.pyplot as plt

from figure import Figure

class MoneyWelfareFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        for session in sessions:
            money = []
            welfare = []
            
            money.append(session.challenge1.money)
            money.append(session.challenge2.money)
            money.append(session.challenge3.money)

            welfare.append(session.challenge1.welfare)
            welfare.append(session.challenge2.welfare)
            welfare.append(session.challenge3.welfare)

            plt.plot(welfare, money, 'k-', linewidth = 0.2)
            plt.plot(welfare[0], money[0], 'rD')
            plt.plot(welfare[1], money[1], 'go')
            plt.plot(welfare[2], money[2], 'bx')

        self.set_x_label("Welfare")
        self.set_y_label("Earnings")
            

