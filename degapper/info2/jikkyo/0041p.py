class Singer:
    def __init__(self, words):
        self.__lyrics = words
    def sing(self):
        print(self.__lyrics)
mysinger = Singer('ドレミ')