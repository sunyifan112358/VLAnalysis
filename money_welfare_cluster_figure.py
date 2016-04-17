import matplotlib.pyplot as plt

from figure import Figure
from color_provider import ColorProvider

class MoneyWelfareClusterFigure(Figure):
    
    def __init__(self):
        pass
        
    def draw(self, sessions):
        self.collect_data(sessions)
        self.process_data()

        self.draw_all_connections()
        self.draw_clusters()

    def collect_data(self, sessions):
        self.data = [[], [], []]
        self.connection = []

        self.money_avg, self.welfare_avg = self.get_mean(sessions)

        for session in sessions:
            if not session.give_recommendation():
                continue

            self.collect_challenge_data(session, 0);
            self.collect_challenge_data(session, 1);
            self.collect_challenge_data(session, 2);

            self.add_connections(session)
    
    def collect_challenge_data(self, session, challenge_id):
        challenge = session.challenge[challenge_id]
        cluster = session.cluster_tags[
                '_money_welfare_' + str(challenge_id)] - 1
        
        while len(self.data[challenge_id]) - 1 < cluster:
            self.data[challenge_id].append([])

        data_list = self.data[challenge_id][cluster]
        data_list.append((challenge.money - self.money_avg[challenge_id], 
                    challenge.welfare - self.welfare_avg[challenge_id]))

    def add_connections(self, session):
        self.connection.append((0, session.cluster_tags['_money_welfare_0'] - 1, 
                1, session.cluster_tags['_money_welfare_1'] - 1))
        self.connection.append((1, session.cluster_tags['_money_welfare_1'] - 1, 
                2, session.cluster_tags['_money_welfare_2'] - 1))
        self.connection.append((0, session.cluster_tags['_money_welfare_0'] - 1, 
                2, session.cluster_tags['_money_welfare_2'] - 1))

    def process_data(self):
        self.cluster_centers = []
        for challenge in self.data:
            self.cluster_centers.append([])
            for cluster in challenge:
                money_sum = 0
                welfare_sum = 0
                point_count = 0
                for point in cluster:
                    money_sum += point[0]
                    welfare_sum += point[1]
                    point_count += 1
                self.cluster_centers[-1].append(
                        (1.0 * money_sum/point_count, 
                        1.0 * welfare_sum/point_count))

                
    def draw_clusters(self):
        for challenge in self.cluster_centers:

            color_list = None
            marker_style = ''
            if challenge == self.cluster_centers[0]:
                color_list = ColorProvider.r
                marker_style = 'D'
            elif challenge == self.cluster_centers[1]:
                color_list = ColorProvider.g
                marker_style = 'o'
            elif challenge == self.cluster_centers[2]:
                color_list = ColorProvider.b
                marker_style = '^'

            cluster_id = 0
            for cluster in challenge:    
                color = color_list[cluster_id * 2]
                plt.plot(cluster[1], cluster[0], marker_style, 
                        color = color, markersize = 12)
                cluster_id += 1

    def draw_all_connections(self):
        c1 = self.cluster_centers[0]
        c2 = self.cluster_centers[1]
        c3 = self.cluster_centers[2]

        for i in range(len(c1)):
            for j in range(len(c2)):
                self.draw_line(0, i, 1, j, ColorProvider.r[0])

        for i in range(len(c2)):
            for j in range(len(c3)):
                self.draw_line(1, i, 2, j, ColorProvider.g[0])

        for i in range(len(c1)):
            for j in range(len(c3)):
                self.draw_line(0, i, 2, j, ColorProvider.b[0])



    def draw_line(self, from_challenge, from_cluster, 
            to_challenge, to_cluster, color):
        connection_count = 0
        for connection in self.connection:
            if connection[0] == from_challenge and \
                connection[1] == from_cluster and \
                connection[2] == to_challenge and \
                connection[3] == to_cluster:
                    connection_count += 1

        line_thickness = connection_count * 0.5

        y = [self.cluster_centers[from_challenge][from_cluster][0], 
                self.cluster_centers[to_challenge][to_cluster][0]]
        x = [self.cluster_centers[from_challenge][from_cluster][1], 
                self.cluster_centers[to_challenge][to_cluster][1]]
        plt.plot(x, y, 'k', linewidth = line_thickness, color = color)

    def get_mean(self, sessions):
        money = [[], [], []]
        welfare = [[], [], []]

        money_avg = [0, 0, 0]
        welfare_avg = [0, 0, 0]

        for session in sessions:
            for i in range(len(session.challenge)):
                money[i].append(session.challenge[i].money)
                welfare[i].append(session.challenge[i].welfare)

        for i in range(len(money)):
            money_avg[i] = sum(money[i])/len(money[i])
            welfare_avg[i] = sum(welfare[i])/len(welfare[i])

        return money_avg, welfare_avg





