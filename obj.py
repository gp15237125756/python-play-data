class Dog:
    """define function"""
    counter = 0

    def __init__(self, name):
        self.name = name
        Dog.counter += 1

    def sayHi(self):
        print('hi, %s' % self.name)
        print('counter: %s' % Dog.counter)

    def setName(self, name):
        self.name = name


if __name__ == "__main__":
    d = Dog("xiaoming")
    d.sayHi()
