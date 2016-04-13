from scipy.stats import linregress
import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class AcceptanceMoneyFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        
        c2_acceptance = []
        c2_money = []
        c3_acceptance = []
        c3_money = []

        for session in sessions:
            c1 = session.challenge1
            c2 = session.challenge2
            c3 = session.challenge3
            acceptance_rate = [
                c2.get_recommendation_acceptance_rate(),
                c3.get_recommendation_acceptance_rate(),
            ]
            money = [
                c2.money, c3.money
            ]

            c2_acceptance.append(c2.get_recommendation_acceptance_rate())
            c2_money.append(c2.money)
            c3_acceptance.append(c3.get_recommendation_acceptance_rate())
            c3_money.append(c3.money)


            plt.plot(acceptance_rate, money, 'k-', linewidth = 0.2)
            plt.plot(acceptance_rate[0], money[0], 'go')
            plt.plot(acceptance_rate[1], money[1], 'bx')
            

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
        self.set_y_label("Earnings")
         
            
