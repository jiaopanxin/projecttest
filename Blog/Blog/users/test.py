import abc

# 这是一个抽象类


class Animal(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def talk(self):
        pass


class Car(Animal):
    def __init__(self):
        pass

    def run(self):
        print('run')

    def talk(self):
        print('talk')


car = Car()
car.run()
