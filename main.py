from Equation import Equation
from OneStepEquation import OneStepEquation
from TwoStepEquation import TwoStepEquation


if __name__ == "__main__":
    for _ in range(10):
        eq = Equation.create()
        print(eq)
        print(eq.representation)
        print(eq.solution)
