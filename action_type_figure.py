from figure import Figure
from priority_action import PriorityAction
from color_provider import ColorProvider

import numpy as np
import matplotlib.pyplot as plt
from operator import add

class ActionTypeFigure(Figure):

    def __init__(self):
        super(ActionTypeFigure, self).__init__()

        self.goals = [
            (-640000, 0.5), 
            (2600000, 0.5),
            (2500000, 1.5)
        ]

    def set_challenge_number(self, challenge_number):
        self.challenge_number = challenge_number

    def draw(self, sessions):
        win_sessions, lose_sessions = self.collect_data(sessions)
        ranked_sessions = self.rank_data(win_sessions, lose_sessions)
        action_count = self.get_action_count(ranked_sessions)
    
        self.plot_figure(ranked_sessions, action_count, len(win_sessions))


    def collect_data(self, sessions):
        win_sessions = []
        lose_sessions = []

        for session in sessions:
            if len(session.challenge) <= self.challenge_number:
                continue
            
            challenge = session.challenge[self.challenge_number]
            if challenge.money >= self.goals[self.challenge_number][0] and \
                challenge.welfare >= self.goals[self.challenge_number][1]:
                    win_sessions.append(session)
            else:
               lose_sessions.append(session)

        return win_sessions, lose_sessions

    def rank_data(self, win_sessions, lose_sessions):
        win_sessions.sort(key = lambda x: x.challenge[
                self.challenge_number].money, reverse=True)
        lose_sessions.sort(key = lambda x: x.challenge[
                self.challenge_number].money, reverse=True)
        return win_sessions + lose_sessions
        '''
        sessions = win_sessions + lose_sessions
        sessions.sort(key = lambda x: x.challenge[self.challenge_number].money,
                reverse = True)
        return sessions
        '''
        '''
        sessions = win_sessions + lose_sessions
        sessions.sort(key = lambda x: 
                x.challenge[self.challenge_number].money / 6000000 + \
                x.challenge[self.challenge_number].welfare,
                reverse = True)
        return sessions
        '''



    def get_action_count(self, sessions):
        action_count = []
        for session in sessions:
            challenge = session.challenge[self.challenge_number]
            action_count.append(self.get_action_count_for_challenge(challenge))

        return action_count

    def get_action_count_for_challenge(self, challenge):
        action_count = [0, 0, 0, 0, 0]
        for action in challenge.actions:
            if isinstance(action, PriorityAction):
                if action.priority <= 1:
                    action_count[0] += 1
                elif action.priority <= 3:
                    action_count[1] += 1
                elif action.priority <= 8:
                    action_count[2] += 1
                elif action.priority <= 20:
                    action_count[3] += 1
                else:
                    action_count[4] += 1
        return action_count

    def plot_figure(self, sessions, action_count, win_count):
        position = np.arange(len(sessions)) + 0.1
        
        color_provider = ColorProvider()  
        bottom = [0] * len(position)
        labels = ['1', '2-3', '4-8', '9-20', '21+']
        bars = []
        for i in range(len(action_count[0])):
            data = [x[i] for x in action_count]
            bar = plt.bar(position, data,
                    width = 0.8,
                    bottom = bottom,
                    color = color_provider[i])
            bars.append(bar)
            bottom = map(add, bottom, data)

        plt.legend(bars, labels)

        
        plt.plot((win_count, win_count), 
                (0, 200),
                'k-')
        plt.xticks(position + 0.4,
                [str(s.id) for s in sessions], rotation = 90)


