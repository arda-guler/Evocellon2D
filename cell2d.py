class cell_bool: # boolean cell, is either one or zero
    def __init__(self, index, state=False):
        self.index = index
        self.state = state

    def set_state(self, state):
        self.state = state
