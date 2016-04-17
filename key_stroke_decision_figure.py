import matplotlib.pyplot as plt
import numpy as np

from figure import Figure
from key_stroke_action import KeyStrokeAction
from phase_action import PhaseAction

class KeyStrokeDecisionFigure(Figure):
    
    def __init__(self):
        pass

    def draw(self, sessions):

        for session in sessions:
            data = [[], [], []]

            for i in range(len(session.challenge)):
                challenge = session.challenge[i]
                data[i] = self.process_challenge(challenge)

            c1_step = 1.0 / (len(c1_data))
            c2_step = 1.0 / (len(c2_data))
            c3_step = 1.0 / (len(c3_data))

            x = []
            curr = 0
            for i in range(len(c1_data)):
                x.append(curr)
                curr += c1_step
            for i in range(len(c2_data)):
                x.append(curr)
                curr += c2_step
            for i in range(len(c3_data)):
                x.append(curr)
                curr += c3_step

            plt.plot(x, c1_data + c2_data + c3_data, '-ko', linewidth = 0.2)
               


            
    def process_challenge(self, challenge):
        count = []
        is_in_decision = False
    
        for action in challenge.actions:
            if isinstance(action, PhaseAction) and action.phase == "Decision":
                count.append(0)
                is_in_decision = True
            elif isinstance(action, PhaseAction) and action.phase == "Simulation":
                is_in_decision = False
            elif is_in_decision and isinstance(action, KeyStrokeAction):
                count[-1] += 1

        return count



