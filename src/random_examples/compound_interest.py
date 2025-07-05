import logging

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    logging.basicConfig(
        filename="compound_interest_log.log",
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s - %(message)s",
    )

    logging.info("New User!")
    print("How many years will you be saving?")
    years = int(input("Enter years: "))
    log_msg1 = "The user is investing for {} years".format(years)
    logging.info(log_msg1)

    print("How much money do you currently have?")
    principle = float(input("Enter how much money you currently have: "))
    log_msg2 = "The user currently has ${:,.2f}".format(principle)
    logging.info(log_msg2)

    print("How much money do you plan on investing monthly?")
    monthly_investment = float(input("Enter ammount: "))
    log_msg3 = "The user is investing ${:,.2f} monthly".format(monthly_investment)
    logging.info(log_msg3)

    print("What yearly intrest rate are you expecting?")
    interest = float(input("Enter the expected intrest rate in decimals (10% = 0.1): "))
    log_msg4 = "The user's intrest rate is {}".format(interest)
    logging.info(log_msg4)
    print(" ")

    monthly_invest = monthly_investment * 12
    final_ammount = 0

    for i in range(0, years):
        if final_ammount == 0:
            final_ammount = principle

        final_ammount = (final_ammount + monthly_invest) * (1 + interest)

    final = "This is how much money you will have after {} years: ${:,.2f}".format(
        years, final_ammount
    )
    print(final)

    logging.info(
        "This is the user's final balance at the end of the period: ${:,.2f}".format(
            final_ammount
        )
    )

    logging.info("Session over...")
    logging.info("Thank you for using our calculator")
