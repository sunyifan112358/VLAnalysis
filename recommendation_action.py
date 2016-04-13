from action import Action

class RecommendationAction(Action):

    def __init__(self):
        super(RecommendationAction, self).__init__()
        self.accpeted = False
        self.ship_id = 0
        self.priority = 0

