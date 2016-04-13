from scipy.cluster.hierarchy import dendrogram, linkage, cophenet
from scipy.spatial.distance import pdist
from scipy.cluster.vq import whiten
import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class DendrogramFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):
        data = self.prepare_data(sessions)
        print(data)
        data = whiten(data)
        Z = linkage(data, 'ward')
        c, coph_dists = cophenet(Z, pdist(data))
        dendrogram(Z)

    def prepare_data(self, sessions):
        data = []
        for session in sessions:
            point = [
                session.challenge1.money,
                session.challenge1.welfare,
                session.challenge2.money,
                session.challenge2.welfare,
                session.challenge3.money,
                session.challenge3.welfare,
            ]
            data.append(point)

        return data

