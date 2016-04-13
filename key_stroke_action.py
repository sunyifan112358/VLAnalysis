from action import Action

class KeyStrokeAction(Action):

    def __init__(self):
        super(KeyStrokeAction, self).__init__()
        self.key = ""
        self.mouse_x = 0
        self.mouse_y = 0

    def __str__(self):
        return ('Key stroke action: \n' + 
                '\treal_time: ' + str(self.real_time) + '\n'
                '\tvirtual_time: ' + str(self.virtual_time) + '\n'
                '\tkey: ' + self.key + '\n'
                '\tmouse: (' + str(self.mouse_x) + ', ' +
                    str(self.mouse_y) + ')\n'
                )

