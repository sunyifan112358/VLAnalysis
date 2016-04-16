from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, fcluster
from scipy.spatial.distance import pdist
from scipy.cluster.vq import whiten
import matplotlib.pyplot as plt
import numpy as np

from figure import Figure

class DendrogramFigure(Figure):
    
    def __init__(self):
        pass

    def based_on_challenge_number(self, challenge_number):
        self.challenge_number = challenge_number

    def draw(self, sessions):
        self.curr_sessions = sessions
        data = self.prepare_data(sessions)

        data = whiten(data)
        Z = linkage(data, 'ward')
        c, coph_dists = cophenet(Z, pdist(data))
        dendrogram(Z, leaf_label_func = self.get_leaf_label,
            distance_sort = True)

        cluster = fcluster(Z, 4, criterion='distance')
    
        self.tag_sessions(cluster)

    def tag_sessions(self, cluster):
        tag_name = 'money_welfare_' + str(self.challenge_number)
        count = 0
        for session in self.curr_sessions:

            session.cluster_tags[tag_name] = cluster[count]
            count += 1

    def get_leaf_label(self, id):
        return str(self.curr_sessions[id].id)

    def prepare_data(self, sessions):
        data = []
        for session in sessions:
            point = [
                session.challenge[self.challenge_number].money,
                session.challenge[self.challenge_number].welfare,
            ]
            data.append(point)

        return data

