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
        )

        return string

    def get_real_duration(self):
        return self.end_real_time - self.start_real_time

    def add_action(self, action):
        self.actions.append(action)

    def get_action_per_minute(self):
        return self.num_key_action / self.get_real_duration() * 60

    def get_recommendation_acceptance_rate(self):
        if self.total_recommendation == 0:
            return 0
        else:
            return 1.0 * self.accepted_recommendation / \
                    self.total_recommendation

