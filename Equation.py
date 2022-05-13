from random import choice, randint


class Equation:
    def __init__(self, representation, solution):
        self.representation = representation
        self.solution = solution

    def create():
        all_subclasses = [cls for cls in Equation.__subclasses__()]
        return choice([cls for cls in all_subclasses]).create()
