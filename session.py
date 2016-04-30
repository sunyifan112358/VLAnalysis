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
        if len(self.challenge) <= 1:
            return "False"
        return self.challenge[1].give_recommendation

    def finished_all_challenges(self):
        return len(self.challenge) == 3

    def add_run(self, run):
        self.challenge.append(run)

    def is_win(self, challenge_number):
        target_money = 0
        target_welfare = 0

        if challenge_number == 0:
            target_money = -640000
            target_welfare = 0.5
        elif challenge_number == 1:
            target_money = 2600000
            target_welfare = 0.5
        elif challenge_number == 2:
            target_money = 2500000
            target_welfare = 1.5

        challenge = self.challenge[challenge_number]
        if challenge.money >= target_money and \
                challenge.welfare >= target_welfare:
            return True
        else:
            return False
            
    def lose_reason(self, challenge_number):
        target_money = 0
        target_welfare = 0

        if challenge_number == 0:
            target_money = -640000
            target_welfare = 0.5
        elif challenge_number == 1:
            target_money = 2600000
            target_welfare = 0.5
        elif challenge_number == 2:
            target_money = 2500000
            target_welfare = 1.5

        challenge = self.challenge[challenge_number]
        


