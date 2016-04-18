from action import Action

class PhaseAction(Action):

    def __init__(self):
        super(PhaseAction, self).__init__()
        self.phase = "Simulation"
        self.money = 0
        self.welfare = 0
