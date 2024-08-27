
from typing import Callable, Optional
from src.data_structures.stack import Stack

print("\nLet's play Towers of Hanoi!!")


left_stack = Stack()
middle_stack = Stack()
right_stack = Stack()

stacks: list[Stack] = [left_stack, middle_stack, right_stack]
# set up game

num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    int(input("Enter a number greater than or equal to 3\n"))

for i in range(num_disks, 0, -1):
    left_stack.push(i)

num_optimal_moves = 2**num_disks - 1

print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")


def get_input():
    choices = [stack.__qualname__[0] for stack in stacks]
    while True:
        for i, val in enumerate(stacks):

            name = val.__qualname__

            letter = choices[i]

            print(f"Enter {name} for {letter}")

        user_input = input("")
        if user_input in choices:
            for i, val in enumerate(stacks):
                if user_input == choices[i]:
                    return val



class Game:

    def __init__(self) -> None:

        self.num_moves = 0


    def main_loop(self) -> Optional[Callable]:

        if right_stack.get_size() != num_disks:
            print("\n\n\n...Current Stacks...")
            for stack in stacks:
                stack.print_items()

            def move() -> Callable:

                print("\nWhich stack do you want to move from?\n")
                from_stack = get_input()
                print("\nWhich stack do you want to move to?\n")
                to_stack = get_input()

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

    def exit_game(self):

        print(
            f"\n\nYou completed the game in {self.num_moves} moves, and the optimal number of moves is {num_optimal_moves}"
        )

if __name__ == '__main__':

    Game().main_loop()