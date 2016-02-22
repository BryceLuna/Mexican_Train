


class Player(object):
    def __init__(self):
        self.hand = []
        #need some way to populate the hand based on the number of players
        self.train = []

    def receive_domino(self, domino):
        self.hand.append(domino)
