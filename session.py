class Session(object):
    
    def __init__(self):
        self.challenge1 = None
        self.challenge2 = None
        self.challenge3 = None

    def __str__(self):
        string = ("Session: \n"
            "challenge1: " + str(self.challenge1) + "\n"
            "challenge2: " + str(self.challenge2) + "\n"
            "challenge3: " + str(self.challenge3) + "\n")
        return string
        
    
