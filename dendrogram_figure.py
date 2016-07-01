from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, fcluster
from scipy.spatial.distance import pdist
from scipy.cluster.vq import whiten
import matplotlib.pyplot as plt
import numpy as np
import sys

from figure import Figure
from color_provider import ColorProvider
from decision_matrix import DecisionMatrix

class DendrogramFigure(Figure):

    def __init__(self):
        self.whiten_enabled = False

    def based_on_challenge_number(self, challenge_number):
        self.challenge_number = challenge_number

    def based_on_item(self, item):
        self.item = item

    def set_threshold(self, threshold):
        self.threshold = threshold

    def enable_whiten(self):
        self.whiten_enabled = True

    def draw(self, sessions, global_stat):
        self.curr_sessions = sessions
        data = self.prepare_data(sessions, global_stat)

        if self.whiten_enabled:
            data = whiten(data)

        Z = linkage(data, 'ward')
        # c, coph_dists = cophenet(Z, pdist(data))
        dendrogram(Z, leaf_label_func = self.get_leaf_label,
            distance_sort = 'descending',
            orientation = 'right',
            color_threshold = self.threshold)

        cluster = fcluster(Z, self.threshold, criterion='distance')

        self.tag_sessions(cluster)
        self.set_y_label("Player ID")
        self.ax.set_xticks([])
        self.ax.yaxis.set_label_position("right")

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
        #return self.session_to_cluster[id].name

    def get_leaf_color(self, group_id):
        color_provider = ColorProvider()
        return color_provider[group_id]

    def prepare_data(self, sessions, global_stat):
        data = []
        self.session_to_cluster = []
        for session in sessions:
            point = []
            for i in range(len(session.challenge)):
                if i in self.challenge_number:
                    if len(session.challenge) <= i:
                        continue
                    challenge = session.challenge[i]

                    if 'welfare' in self.item:
                        point.append(challenge.welfare)
                    if 'money' in self.item:
                        point.append(challenge.money)
                    if 'action_type' in self.item:
                        point.append(challenge.get_num_priority_change(0, 1))
                        point.append(challenge.get_num_priority_change(2, 3))
                        point.append(challenge.get_num_priority_change(4, 8))
                        point.append(challenge.get_num_priority_change(9, 20))
                        point.append(challenge.get_num_priority_change(21,
                                    sys.maxint))
                    if 'action_matrix' in self.item:
                        point += self.get_decision_matrix_as_list(challenge)

            target_point_length = len(self.challenge_number) * len(self.item)
            if 'action_type' in self.item:
                target_point_length += 4 * len(self.challenge_number)
            if 'action_matrix' in self.item:
                target_point_length = 570 * len(self.challenge_number)

            if len(point) == target_point_length:
                data.append(point)
                self.session_to_cluster.append(session)

        return data

    def get_decision_matrix_as_list(self, challenge):
        decision_matrix_extractor = DecisionMatrix()
        decision_matrix = decision_matrix_extractor.extract_decision_matrix(
                challenge)

        data = []
        for ship_decision in decision_matrix:
            data += ship_decision

        return data
