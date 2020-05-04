class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, {0}'.format(self.name))

p = Person('Shiv Shankar')
p.say_hi()