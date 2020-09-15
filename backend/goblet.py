import random


class Goblet:
    def __init__(self):
        self.goblet = []
        self.count = [0] * 6

    def shake(self):
        for self.dice in range(5):
            self.goblet.append(random.randint(1, 6))
        return self.goblet

    def goblet_value(self):
        for dice in self.goblet:
            if dice == 1:
                for value in range(1, len(self.count)):
                    self.count[value] += 1
            self.count[dice - 1] += 1
        return self.count


if __name__ == "__main__":
    goblet = Goblet()
    goblet.shake()
    print(goblet.goblet)
    goblet.goblet_value()
    print(goblet.count)