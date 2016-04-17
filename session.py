class Session(object):
    
    def __init__(self):
        self.name = ""
        self.id = 0
        self.cluster_tags = {}
        self.bg_tag = ""

        self.challenge = []

    def __str__(self):
        string = ("Session (" + str(self.id) + "): " + self.name + "\n"
            "give_recommendation: " + str(self.give_recommendation()) + "\n"
            "bg_tag: " + str(self.bg_tag) + "\n"
            "cluster_tags: " + str(self.cluster_tags) + "\n")
        
        for i in range(len(self.challenge)):
            challenge = self.challenge[i]
            string += "challenge" + str(i) +": " + str(self.challenge[i]) + "\n"

        return string

    def give_recommendation(self):
        if len(self.challenge) == 1:
            return "Unknown"
        return self.challenge[1].give_recommendation

    def finished_all_challenges(self):
        return len(self.challenge) == 3

    def add_run(self, run):
        self.challenge.append(run)

        
