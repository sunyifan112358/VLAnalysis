class Session(object):
    
    def __init__(self):
        self.name = ""
        self.id = 0
        self.cluster_tags = {}
        self.bg_tag = ""

        self.challenge = [None, None, None]

    def __str__(self):
        string = ("Session (" + str(self.id) + "): " + self.name + "\n"
            "give_recommendation: " + str(self.give_recommendation()) + "\n"
            "bg_tag: " + str(self.bg_tag) + "\n"
            "cluster_tags: " + str(self.cluster_tags) + "\n"
            "challenge1: " + str(self.challenge[0]) + "\n"
            "challenge2: " + str(self.challenge[1]) + "\n"
            "challenge3: " + str(self.challenge[2]) + "\n")
        return string

    def give_recommendation(self):
        if self.challenge[2] == None:
            return "Unknown"
        return self.challenge[2].give_recommendation
        
    
