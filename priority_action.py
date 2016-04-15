from action import Action

class PriorityAction(Action):

    def __init__(self):
        super(PriorityAction, self).__init__()
        self.ship_id = 0
        self.priority = 0

