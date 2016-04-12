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
            "\tactions: "
        )

        for action in self.actions:
            string += str(action)

        string += "\n"

        return string

