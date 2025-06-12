import random
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="magic_8_ball_log.log",
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
)

logging.info("New User!!")
name = input("Tell me your name: ")
logging.info("The user's name is {}".format(name))

question = input("Ask me your question: ")
logging.info("The user asked: {}".format(question))

# if not isinstance(question, str):
#    print("You need to input a string!")
#    logging.WARNING("The user inputed something other than a string")
#    quit()

random_number = random.randint(1, 9)
logging.info("The random number is {}".format(random_number))
answer = ""


def statements(random_number):

    if random_number == 1:
        answer = "Yes - definitely."
    elif random_number == 2:
        answer = "It is decidedly so."
    elif random_number == 3:
        answer = "Without a doubt."
    elif random_number == 4:
        answer = "Reply hazy, try again."
    elif random_number == 5:
        answer = "Ask again later."
    elif random_number == 6:
        answer = "Better not tell you now."
    elif random_number == 7:
        answer = "My sources say no."
    elif random_number == 8:
        answer = "Outlook not so good."
    elif random_number == 9:
        answer = "Very doubtful."
    else:
        answer = "Error!"
    return answer


logging.info("The 8-ball answered: {}".format(statements(random_number)))
# print('{name} asks: {question}'.format(name = name, question = question))
print("Magic 8-Ball's answer: " + statements(random_number))

logging.info("Session over!")