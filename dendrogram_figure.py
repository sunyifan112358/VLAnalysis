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
                session.challenge1.get_real_duration(),
                session.challenge1.get_action_per_minute(),
#session.challenge1.get_recommendation_acceptance_rate(),
                session.challenge2.money,
                session.challenge2.welfare,
                session.challenge2.get_real_duration(),
                session.challenge2.get_action_per_minute(),
                session.challenge2.get_recommendation_acceptance_rate(),
                session.challenge3.money,
                session.challenge3.welfare,
                session.challenge3.get_real_duration(),
                session.challenge3.get_action_per_minute(),
                session.challenge3.get_recommendation_acceptance_rate(),
            ]
            data.append(point)

        return data

