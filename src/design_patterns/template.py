"""

the template patter is a behavioral design pattern that defines the
program skeleton of an algorithm
in the superclass but lets subclasses override specific steps of
the algorithm without changing its structure.

"""

from typing import Protocol, Callable


class AlgoirthmTemplate(Protocol):
    """
    define the steps of the algorithm
    these can be abstract methods that are implemented by subclasses
    """

    def step1(self): ...

    def step2(self): ...

    def step3(self): ...


class ConcreteAlgorithm1(AlgoirthmTemplate):
    """
    implement the steps of the algorithm
    """

    def step1(self):
        print("ConcreteAlgorithm1 step1")

    def step2(self):
        print("ConcreteAlgorithm1 step2")

    def step3(self):
        print("ConcreteAlgorithm1 step3")


class ConcreteAlgorithm2(AlgoirthmTemplate):
    """
    implement the steps of the algorithm
    """

    def step1(self):
        print("ConcreteAlgorithm2 step1")

    def step2(self):
        print("ConcreteAlgorithm2 step2")

    def step3(self):
        print("ConcreteAlgorithm2 step3")


# Functional approach
def execute_template(step1: Callable, step2: Callable, step3: Callable):
    """
    functional approach

    the steps are passed as arguments to the function
    they can be "any" function that takes no arguments
    """
    step1()
    step2()
    step3()
