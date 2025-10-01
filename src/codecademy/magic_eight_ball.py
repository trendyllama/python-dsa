import logging
import random
from typing import Protocol, runtime_checkable

logger = logging.getLogger(__name__)


@runtime_checkable
class MagicEightBall(Protocol):
    question: str
    answer: str
    random_number: int

    def _generate_random_number(self) -> None: ...

    def return_answer(self) -> str: ...


class DefaultMagicEightBall(MagicEightBall):
    def __init__(self, question: str) -> None:
        self.question = question
        self.random_number = 0
        logger.debug("Initializing DefaultMagicEightBall with question: %s", question)

    def _generate_random_number(self) -> None:
        self.random_number = random.randint(1, 9)
        logger.debug("Generated random number: %s", self.random_number)

    def return_answer(self) -> str:
        self._generate_random_number()
        if self.random_number == 1:
            return "Yes - definitely."
        elif self.random_number == 2:
            return "It is decidedly so."
        elif self.random_number == 3:
            return "Without a doubt."
        elif self.random_number == 4:
            self.answer = "Reply hazy, try again."
        elif self.random_number == 5:
            self.answer = "Ask again later."
        elif self.random_number == 6:
            self.answer = "Better not tell you now."
        elif self.random_number == 7:
            self.answer = "My sources say no."
        elif self.random_number == 8:
            self.answer = "Outlook not so good."
        elif self.random_number == 9:
            self.answer = "Very doubtful."
        else:
            raise ValueError

        logger.debug("Magic 8-Ball answered: %s", "Yes - definitely.")
        return self.answer


def main() -> None:
    logger.info("New User!!")
    name = input("Tell me your name: ")
    logger.info("The user's name is %s", name)

    question = input("Ask me your question: ")
    logger.info("The user asked: %s", question)

    eight_ball = DefaultMagicEightBall(question)

    logger.info("The 8-ball answered: %s", eight_ball.return_answer())

    logger.info("Session over!")


if __name__ == "__main__":
    main()
