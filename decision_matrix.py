from phase_action import PhaseAction
from priority_action import PriorityAction

class DecisionMatrix(object):

    def __init__(self):
        pass

    def extract_decision_matrix(self, challenge):
        num_ships = 30
        matrix = [[] for i in range(num_ships)]

        in_decision = False
        cycle = 0
        for action in challenge.actions:
            if isinstance(action, PhaseAction) and action.phase == "Decision":        
                self.add_new_decision_phase(matrix)
                in_decision = True
            elif isinstance(action, PriorityAction):
                matrix[action.ship_id - 1][-1] = 1.0 / action.priority
            elif isinstance(action, PhaseAction) and \
                    action.phase == "Simulation" and \
                    in_decision == True:
                in_decision = False

                if cycle >= 1:
                    for ship_decision in matrix:
                        if ship_decision[-1] == 0:
                            ship_decision[-1] = ship_decision[-2]
                cycle += 1


        return matrix

    def add_new_decision_phase(self, matrix):
        for ship_action_list in matrix:
            ship_action_list.append(0)
            

