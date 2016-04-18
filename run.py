from cleaning_action import CleaningAction
from priority_action import PriorityAction
from phase_action import PhaseAction

class Run(object):
    
    def __init__(self):
        self.actions = []

        self.start_real_time = 0;
        self.give_recommendation = False
        self.with_justification = False
        self.map_file = ''
        self.is_tutorial = False
        
        self.end_real_time = 0
        self.money = 0
        self.welfare = 0
        self.dock_utilization = 0

        self.num_key_action = 0
        self.accepted_recommendation = 0
        self.total_recommendation = 0


    def __str__(self):
        string = ("Run: "
            "" + self.map_file + "\n"
            "\tstart_real: " + str(self.start_real_time) + "\n"
            "\tend_real: " + str(self.end_real_time) + "\n"
            "\tmoney: " + str(self.money) + "\n"
            "\twelfare: " + str(self.welfare) + "\n"
            "\tdock_utilization: " + str(self.dock_utilization) + "\n"
            "\tgive_recommendation: " + str(self.give_recommendation) + "\n"
            "\twith_justification: " + str(self.with_justification) + "\n"
            "\tis_tutorial: " + str(self.is_tutorial) + "\n"
            "\tnum_action: " + str(len(self.actions)) + "\n"
            "\tnum_key_action: " + str(self.num_key_action) + "\n"
            "\tnum_recommendation: " + str(self.total_recommendation) + "\n"
            "\tnum_accepted_recommendation: " + 
                str(self.accepted_recommendation) + "\n"
            "\toil_cleaning_solution: " + 
                self.get_oil_cleaning_solution() + '\n'
        )

        return string

    def get_real_duration(self):
        return self.end_real_time - self.start_real_time

    def add_action(self, action):
        self.actions.append(action)

    def get_action_per_minute(self):
        return self.num_key_action / self.get_real_duration() * 60

    def get_num_priority_change(self, min_priority = 0, max_priority = 100):
        count = 0
        for action in self.actions:
            if isinstance(action, PriorityAction):
                if action.priority >= min_priority and \
                    action.priority <= max_priority:
                        count += 1        
        return count

    def get_total_decision_time(self):
        count = 0
        decision_start_time = 0
        for action in self.actions:
            if isinstance(action, PhaseAction) and action.phase == "Decision":
                decision_start_time = action.real_time
            elif decision_start_time != 0 and isinstance(action, PhaseAction) \
                and action.phase == "Simulation":
                count += (action.real_time - decision_start_time)
                decision_start_time = 0
        return count

    def get_recommendation_acceptance_rate(self):
        if self.total_recommendation == 0:
            return 0
        else:
            return 1.0 * self.accepted_recommendation / \
                    self.total_recommendation

    def get_oil_cleaning_solution(self):
        solution = "None"
        for action in self.actions:
            if isinstance(action, CleaningAction):
                solution = action.solution
        return solution


    def get_pri_money(self, challenge_id, global_stat):
        money_avg, welfare_avg = global_stat.get_mean(challenge_id,
                self.get_oil_cleaning_solution())
        return self.money - money_avg

    def get_pri_welfare(self, challenge_id, global_stat):
        money_avg, welfare_avg = global_stat.get_mean(challenge_id,
                self.get_oil_cleaning_solution())
        return self.welfare - welfare_avg
