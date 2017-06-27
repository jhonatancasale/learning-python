"""from: https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3"""

class Pizza():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("Pizza created: %s ($%d)", self.name, self.price)

    def make(self, quantity=1):
        print("Made %d %s pizza(s)", quantity, self.name)

    def eat(self, quantity=1):
        print("Ate %d %s pizza(s)", quantity, self.name)


pizza_01 = Pizza("artichoke", 15)
pizza_01.make()
pizza_01.eat()

pizza_02 = Pizza("margherita", 12)
pizza_02.make(2)
pizza_02.eat()
