import matplotlib.pyplot as plt

class Figure(object):
    
    def __init__(self):
        pass

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def initialize(self):
        self.fig, self.ax = plt.subplots(figsize = (self.width, self.height))

    def set_font_size(self, font_size):
        self.font_size = font_size

    def set_x_label(self, label):
        self.ax.set_xlabel(label, fontsize = self.font_size)

    def set_y_label(self, label):
        self.ax.set_ylabel(label, fontsize = self.font_size)

    def show(self):
        plt.show()

    def save_eps(self, file_name):
        plt.tight_layout()
        plt.savefig(file_name, format='eps', bbox_inches='tight', 
                pad_inches = 0)
