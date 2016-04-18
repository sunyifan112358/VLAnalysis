class GlobalStat(object):

    def __init__(self):
        pass

    def calculate(self, sessions):
        self.sessions = sessions

    def get_mean(self, challenge_num, oil_cleaning = "All"):
        money = []
        welfare = []
        for session in self.sessions:
            if len(session.challenge) <= challenge_num:
                continue

            challenge = session.challenge[challenge_num]
            
            if oil_cleaning == "All" or \
                oil_cleaning == challenge.get_oil_cleaning_solution():
                money.append(challenge.money)
                welfare.append(challenge.welfare)

        money_avg = sum(money)/len(money)
        welfare_avg = sum(welfare)/len(welfare)

        return money_avg, welfare_avg

