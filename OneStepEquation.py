from random import choice, randint
from Equation import Equation


# Class definition and all subclasses of one-step equations.
class OneStepEquation(Equation):
    def create():
        return choice([cls for cls in OneStepEquation.__subclasses__()]).create()

    def __repr__(self) -> str:
        return "OneStepEquation"


class OneStepAddition(OneStepEquation):
    def create():
        a, b = randint(-10, 20), randint(-20, 30)
        return OneStepEquation(f'x+{a}={b}', f'{b-a}')


class OneStepSubtraction(OneStepEquation):
    def create():
        a, b = randint(-10, 20), randint(-20, 30)
        return OneStepEquation(f'x-{a}={b}', f'{b+a}')


class OneStepMultiplication(OneStepEquation):
    def create():
        a, b = randint(2, 10), randint(-10, 11)
        return OneStepEquation(f'x/{a}={b}', f'{b*a}')


class OneStepDivision(OneStepEquation):
    def create():
        a, b = randint(2, 10), randint(2, 5)
        return OneStepEquation(f'{a}x={b*a}', f'{b}')


if __name__ == "__main__":
    for _ in range(10):
        eq = OneStepEquation.create()
        print(eq)
        print(eq.representation)
        print(eq.solution)
