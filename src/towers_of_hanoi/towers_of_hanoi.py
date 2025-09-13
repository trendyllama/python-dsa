import enum
import logging
import sys
from collections.abc import Callable
from typing import Protocol

from src.data_structures.stack import Stack

# set up game

logger = logging.getLogger(__name__)

class GameStates(enum.Enum):
    INVALID_MOVE = 0


class InputError(Exception): ...

class TowersOfHanoiInterface(Protocol):

    num_moves: int
    num_disks: int
    num_optimal_moves: int
    stacks: list[Stack]

    def __init__(self, number_of_disks: int) -> None: ...

    def get_input(self) -> Stack: ...

    def exit_game(self) -> None: ...

    def run(self) -> None: ...


class Game(TowersOfHanoiInterface):
    def __init__(self, number_of_disks: int) -> None:
        self.num_moves = 0
        self.num_disks = number_of_disks

        logger.info("Let's play Towers of Hanoi!!")

        left_stack = Stack()
        middle_stack = Stack()
        self.right_stack = Stack()

        self.stacks: list[Stack] = [left_stack, middle_stack, self.right_stack]


        for i in range(self.num_disks, 0, -1):
            left_stack.push(i)

        self.num_optimal_moves = 2**self.num_disks - 1

        logger.info(
            "The fastest you can solve this game is in %s moves", self.num_optimal_moves
        )

    def get_input(self) -> Stack:
        choices = [stack.__qualname__[0] for stack in self.stacks]

        while True:
            for i, val in enumerate(self.stacks):
                name = val.__qualname__

                letter = choices[i]

                logger.info("Enter %s for %s", name, letter)

            user_input = input("")
            if user_input in choices:
                for i, val in enumerate(self.stacks):
                    if user_input == choices[i]:
                        return val

    def exit_game(self) -> None:
        logger.info(
            "You completed the game in %s moves, and the optimal number of moves is %s",
            self.num_moves,
            self.num_optimal_moves,
        )
        sys.exit(0)

    def run(self) -> None:


        def runner():
            if self.right_stack.size != self.num_disks:
                logger.info("Current Stacks...")
                for stack in self.stacks:
                    logger.info(stack)

                def move() -> Callable | None:
                    logger.info("Which stack do you want to move from?\n")
                    from_stack = self.get_input()

                    if from_stack is None:
                        logger.info("Invalid Move. Try Again")

                        return move()

                    logger.info("Which stack do you want to move to?\n")
                    to_stack = self.get_input()

                    if from_stack.size == 0 or from_stack is None:
                        logger.info("Invalid Move. Try Again")

                        return move()

                    if to_stack.size == 0 or from_stack.peek().value < to_stack.peek().value:
                        disk = from_stack.pop()
                        to_stack.push(disk)

                        self.num_moves += 1
                        return self.exit_game()

                    logger.info("Invalid Move. Try Again")

                    return move()

                return

            else:
                return runner()

        return runner()


class GameBuilder:


    def __init__(self, number_of_disks: int) -> None:
        self.number_of_disks = number_of_disks

    def build(self) -> Game:
        pass


if __name__ == "__main__":
    Game(number_of_disks=15).run()
