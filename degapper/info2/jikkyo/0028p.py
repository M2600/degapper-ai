class LED:
    def __init__(self, s):
        self.__state = s
    def write_digital(self, b):
        print('LED:', self.__state, 'to', b)
        self.__state = b
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, b):
        if b == 0 or b == 1:
            self.__state = b
        else:
            print('illegal setting')