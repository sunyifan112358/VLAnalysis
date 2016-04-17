from scipy.stats import linregress
import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class AcceptanceWelfareFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        
        c2_acceptance = []
        c2_welfare = []
        c3_acceptance = []
        c3_welfare = []

        for session in sessions:
            if not session.finished_all_challenges():
                continue


            c1 = session.challenge[0]
            c2 = session.challenge[1]
            c3 = session.challenge[2]
            acceptance_rate = [
                c2.get_recommendation_acceptance_rate(),
                c3.get_recommendation_acceptance_rate(),
            ]
            welfare = [
                c2.welfare, c3.welfare
            ]

            c2_acceptance.append(c2.get_recommendation_acceptance_rate())
            c2_welfare.append(c2.welfare)
            c3_acceptance.append(c3.get_recommendation_acceptance_rate())
            c3_welfare.append(c3.welfare)


            plt.plot(acceptance_rate, welfare, 'k-', linewidth = 0.2)
            plt.plot(acceptance_rate[0], welfare[0], 'go')
            plt.plot(acceptance_rate[1], welfare[1], 'b^')
            

        slope, intercept, r_value, p_value, std_err = \
                linregress(c2_acceptance, c2_welfare)
        X = np.array(c2_acceptance)
        plt.plot(X, slope * X + intercept, 'g', 
                linewidth = 0.2)

        slope, intercept, r_value, p_value, std_err = \
                linregress(c3_acceptance, c3_welfare)
        X = np.array(c3_acceptance)
        plt.plot(X, slope * X + intercept, 'b', 
                linewidth = 0.2)



        self.set_x_label("Acceptance Rate")
        self.set_y_label("Welfare")
         
 
