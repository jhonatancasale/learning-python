"""from: https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3"""

import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)


class Pizza():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        logging.debug("Pizza created: %s ($%d)" % (self.name, self.price))

    def make(self, quantity=1):
        logging.debug("Made %d %s pizza(s)" % (quantity, self.name))

    def eat(self, quantity=1):
        logging.debug("Ate %d %s pizza(s)" % (quantity, self.name))


pizza_01 = Pizza("artichoke", 18)
pizza_01.make(5)
pizza_01.eat(4)

pizza_02 = Pizza("margherita", 16)
pizza_02.make(2)
pizza_02.eat(2)
