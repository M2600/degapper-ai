class Thermometer:
    def __init__(self, t):
        self.temp = t
    def read_analog(self):
        t = self.temp
        self.temp = t + 1.0
        print('thermometer:', self.temp)
        return self.temp

class LED:
    def __init__(self, s):
        self.state = s
    def write_digital(self, b):
        print('LED:', self.state, 'to', b)
        self.state = b