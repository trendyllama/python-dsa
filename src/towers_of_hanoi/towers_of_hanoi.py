
from collections.abc import Callable
from src.data_structures.stack import Stack

# set up game


class InputError(Exception):
    """ """


class Game:
    def __init__(self) -> None:
        self.num_moves = 0

        print("\nLet's play Towers of Hanoi!!")

        left_stack = Stack()
        middle_stack = Stack()
        self.right_stack = Stack()

        self.stacks: list[Stack] = [left_stack, middle_stack, self.right_stack]

        self.num_disks = int(input("\nHow many disks do you want to play with?\n"))

        num_input = int(input("Enter a number greater than or equal to 3\n"))

        if num_input < 3:
            raise InputError("Enter a number greater or equal to 3")

        for i in range(self.num_disks, 0, -1):
            left_stack.push(i)

        self.num_optimal_moves = 2**self.num_disks - 1

        print(
            f"\nThe fastest you can solve this game is in {self.num_optimal_moves} moves"
        )

    def get_input(self) -> Stack:
        # choices = [stack.__qualname__[0] for stack in self.stacks]
        choices = list(map(lambda x: x.__qualname__[0], self.stacks))

        while True:
            for i, val in enumerate(self.stacks):
                name = val.__qualname__

                letter = choices[i]

                print(f"Enter {name} for {letter}")

            user_input = input("")
            if user_input in choices:
                for i, val in enumerate(self.stacks):
                    if user_input == choices[i]:
                        return val

    def exit_game(self) -> None:
        print(
            f"\n\nYou completed the game in {self.num_moves} moves, and the optimal number of moves is {self.num_optimal_moves}"
        )

    def main_loop(self) -> Callable | None:
        if self.right_stack.get_size() != self.num_disks:
            print("\n\n\n...Current Stacks...")
            for stack in self.stacks:
                stack.print()

            def move() -> Callable | None:
                print("\nWhich stack do you want to move from?\n")
                from_stack = self.get_input()
                print("\nWhich stack do you want to move to?\n")
                to_stack = self.get_input()

                if from_stack.get_size() == 0:
                    print("\n\nInvalid Move. Try Again")

                    return move()

                if to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
                    disk = from_stack.pop()
                    to_stack.push(disk)

                    self.num_moves += 1
                    return self.exit_game()

                print("\n\nInvalid Move. Try Again")

                return move()

            move()

        else:
            return self.main_loop()


if __name__ == "__main__":
    Game().main_loop()
