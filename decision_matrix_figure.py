import matplotlib.pyplot as plt
import matplotlib
import numpy as np

from figure import Figure
from decision_matrix import DecisionMatrix

class DecisionMatrixFigure(Figure):

    def __init__(self):
        pass

    def draw(self, challenge):
        decision_matrix_extractor = DecisionMatrix()
        decision_matrix = decision_matrix_extractor.extract_decision_matrix(challenge)
        print(decision_matrix)

        data = np.array(decision_matrix)

        for p in np.nditer(data, op_flags=['readwrite']):
            if p != 0:
                p[...] = 1.0 / p

        color_map = matplotlib.colors.LinearSegmentedColormap.from_list(
                'custom', ['r', 'b'], N = 256)
        color_map.set_under(color = 'w')
       
                
        plt.pcolor(data, cmap = color_map, vmin = 1, vmax = 20)
        cb = plt.colorbar()
        cb.ax.invert_yaxis()

        self.set_x_label("Decision Phase")
        self.set_y_label("Ship ID")

       
