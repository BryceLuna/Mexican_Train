import itertools
import random

class Domino(object):
    """
    This is a domino. A domino has two integer numbers
    """
    def __init__(self, number1, number2):
        self.num1 = number1
        self.num2 = number2

    def get_numbers(self):
        return (self.num1, self.num2)

    def __repr__(self):
        return "%s, %s" % (self.num1,self.num2)


class Stack(object):
    def __init__(self):
        self.dominos = []
        for dom in itertools.combinations_with_replacement(range(13),2):
            self.dominos.append(Domino(dom[0],dom[1]))

    def get_dominos(self):
        return self.dominos

    def shuffle(self):
        random.shuffle(self.dominos)

    def is_empty(self):
        return self.dominos == []

    def draw_domino(self):
        if not self.is_empty():
            return self.dominos.pop()

    def __len__(self):
        return len(self.dominos)


if __name__ == "__main__":
    print my_test()
