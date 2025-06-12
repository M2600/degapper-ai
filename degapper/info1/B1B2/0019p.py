class Person:
    def __init__(self, name, years):
        self.__name = namae
        self.__age = years
    @property
    def nenrei(self):
        return self.__age
    @nenrei.setter
    def nenrei(self, years):
        self.__age = years
    def profile(self):
        print (self.__name, 'の年齢は', self.__age , 'です')
suzuki = Person('鈴木', 16)
tanaka = Person('田中', 32)
print(suzuki.nenrei)
suzuki.profile()
tanaka.profile()
suzuki.nenrei = 17
suzuki.profile()