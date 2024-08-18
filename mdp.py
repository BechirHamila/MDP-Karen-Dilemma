class MDP:
    def __init__(self):
        self.states = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.actions = {
            1: ('r', 'd'),
            2: ('r', 'd', 'l'),
            3: ('l', 'd'),
            4: ('u', 'r', 'd'),
            5: ('u', 'r', 'd', 'l'),
            6: ('u', 'd', 'l'),
            7: ('u', 'r'),
            8: ('u', 'r', 'l'),
            9: ('u', 'l')
        }

    def getStartState(self):
        return 1

    def isEndState(self, state):
        return state == 9

    def getActions(self, state):
        return self.actions[state]

    def getSuccessorProbReward(self, state, action):
        spr = {
            1: {'r': [(2, 1.0, -1)], 'd': [(4, 1.0, -1)]},
            2: {'r': [(3, 1.0, -1)], 'd': [(5, 1.0, -1)], 'l': [(1, 1.0, -1)]},
            3: {'d': [(6, 0.01, -1), (2, 0.99, -1)], 'l': [(2, 1.0, -1)]},
            4: {'u': [(1, 0.3, -1), (5, 0.3, -1), (7, 0.4, -11)], 
                'r': [(1, 0.3, -1), (5, 0.3, -1), (7, 0.4, -11)], 
                'd': [(1, 0.3, -1), (5, 0.3, -1), (7, 0.4, -11)]},
            5: {'u': [(2, 1.0, -1)], 'r': [(8, 0.7, -1), (6, 0.1, -1), 
                (4, 0.1, -1), (2, 0.1, -1)], 'd': [(8, 1.0, -1)], 'l': [(4, 1.0, -1)]},
            6: {'d': [(9, 1.0, 49)], 'u': [(3, 1.0, -1)], 'l': [(5, 1.0, -1)]},
            7: {'u': [(4, 1.0, -1)], 'r': [(8, 1.0, -1)]},
            8: {'r': [(7, 0.8, -11), (9, 0.1, 49), (5, 0.1, -1)], 
                'l': [(7, 1.0, -11)], 'u': [(5, 1.0, -1)]},
            9: {'l': [(8, 1.0, -1)], 'u': [(6, 0.1, -1)]},
        }
        if state in spr and action in spr[state]:
            return spr[state][action]
        return []

    def getDiscount(self):
        return 1.0

    def getStates(self):
        return self.states