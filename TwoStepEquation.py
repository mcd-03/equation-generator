from random import choice, randint
from Equation import Equation


# Class definition and all subclasses of two-step equations.
class TwoStepEquation(Equation):
    def create():
        return choice([cls for cls in TwoStepEquation.__subclasses__()]).create()

    def __repr__(self) -> str:
        return "TwoStepEquation"


class TwoStepAddition(TwoStepEquation):
    def create():
        a, b, c = randint(2, 10), randint(-10, 15), randint(-10, 15)
        return TwoStepEquation(f'{a}x+{b}={a * c + b}', f'x={c}')


class TwoStepMultiplication(TwoStepEquation):
    def create():
        a, b, c = randint(2, 10), randint(2, 10), randint(-10, 11)
        return TwoStepEquation(f'x/{a} - {b} = {c}', f'x={a * (c + b)}')


class TwoStepDivision(TwoStepEquation):
    def create():
        a, b, c = randint(2, 10), randint(2, 10), randint(-5, 5)
        return TwoStepEquation(f'{a}(x + {b})={a * c}', f'x={c - b}')


if __name__ == "__main__":
    for _ in range(10):
        eq = TwoStepEquation.create()
        print(eq)
        print(eq.representation)
        print(eq.solution)
