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

    def based_on_item(self, item):
        self.item = item

    def draw(self, sessions):
        self.curr_sessions = sessions
        data = self.prepare_data(sessions)

        data = whiten(data)
        Z = linkage(data, 'ward')
        c, coph_dists = cophenet(Z, pdist(data))
        dendrogram(Z, leaf_label_func = self.get_leaf_label,
            distance_sort = True)

        cluster = fcluster(Z, 3, criterion='distance')
    
        self.tag_sessions(cluster)

    def tag_sessions(self, cluster):
        tag_name = self.get_tag_name()
        count = 0
        for session in self.session_to_cluster:
            session.cluster_tags[tag_name] = cluster[count]
            count += 1

    def get_tag_name(self):
        tag_name = ''

        for i in self.item:
            tag_name += '_'
            tag_name += i

        for c in self.challenge_number:
            tag_name += '_'
            tag_name += str(c)

        return tag_name



    def get_leaf_label(self, id):
        return str(self.curr_sessions[id].id)

    def prepare_data(self, sessions):
        data = []
        self.session_to_cluster = []
        for session in sessions:
            point = []
            for i in range(len(session.challenge)):
                if i in self.challenge_number:
                    challenge = session.challenge[i]
                    if challenge == None:
                        continue
                    if 'welfare' in self.item:
                        point.append(challenge.welfare)
                    if 'money' in self.item:
                        point.append(challenge.money)
            
            if len(point) == len(self.challenge_number) * len(self.item):
                data.append(point)
                self.session_to_cluster.append(session)

        return data

