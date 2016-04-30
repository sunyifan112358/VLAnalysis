import matplotlib.pyplot as plt
import numpy as np
from operator import add

from figure import Figure
from phase_action import PhaseAction
from priority_action import PriorityAction
from recommendation_action import RecommendationAction

class DecisionPhaseAcceptanceFigure(Figure):
    
    def __init__(self):
        super(DecisionPhaseAcceptanceFigure, self).__init__()

    def draw(self, sessions):
        accepted, denied = self.collect_data(sessions)

        rate = []    
        for i in range(len(accepted)):
            if accepted[i] + denied[i] == 0:
                rate.append(0)
            else:
                rate.append(1.0 * accepted[i] / (accepted[i] + denied[i]))

        line1 = plt.plot(np.arange(len(accepted)), rate, '-r', 
                label="acceptance rate")
        #line2 = plt.plot(np.arange(len(denied)), denied, '-b',
        #        label="num deny")
        plt.axvline(7)
        plt.axvline(27)

        self.ax.set_xticks([10, 30])
        self.ax.set_xticklabels(["Challenge 2", "Challenge 3"])
        self.ax.set_xticks(np.arange(40), minor=True)
        self.ax.grid(b=True, which='minor', color='k', alpha = 0.4, linestyle='--')
        #plt.legend(loc="lower right")

    def collect_data(self, sessions):
        accepted = []
        denied = []

        for session in sessions:
            if not session.finished_all_challenges():
                continue

            session_accepted = [] 
            session_denied = [] 
            for challenge in session.challenge:
                if challenge == session.challenge[0]:
                    continue
                c_accepted, c_denied = self.get_challenge_data(challenge)
                session_accepted += c_accepted
                session_denied += c_denied

            if len(accepted) == 0:
                accepted = session_accepted
                denied = session_denied
            else:
                accepted = map(add, accepted, session_accepted)
                denied = map(add, denied, session_denied)

        return accepted, denied

    def get_challenge_data(self, challenge):
        accepted = []
        denied = []
        in_decision = False
        cycle = 0
        
        accept_count = 0
        deny_count = 0
        recommendation_list = {}
        for action in challenge.actions:
            if isinstance(action, PhaseAction) and action.phase == "Decision":        
                in_decision = True
            elif isinstance(action, PriorityAction):
                if action.ship_id in recommendation_list:
                    if action.priority == recommendation_list[action.ship_id][0] \
                            and recommendation_list[action.ship_id][1] == False:
                                accept_count += 1
                                deny_count -= 1
                    elif action.priority != recommendation_list[action.ship_id][0] \
                            and recommendation_list[action.ship_id][1] == True:
                                deny_count += 1
                                accept_count -= 1

            elif isinstance(action, RecommendationAction):
                recommendation_list[action.ship_id] = \
                    (action.priority, action.accepted)
                if action.accepted:
                    accept_count += 1
                else:
                    deny_count += 1
            elif isinstance(action, PhaseAction) and \
                    action.phase == "Simulation" and \
                    in_decision == True:
                in_decision = False

                accepted.append(accept_count)
                denied.append(deny_count)

                accept_count = 0
                deny_count = 0
                recommendation_list = {}

        # add 0 to fix length
        while len(accepted) < 20:
            accepted.append(0)
        while len(denied) < 20:
            denied.append(0)

        return accepted, denied

            

