import logging
import tkinter as tk

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.debug("Starting main function")
    root = tk.Tk()

    root.geometry("800x400")

    root.title("First GUI")

    lable = tk.Label(root, text="Hello World!", font=("Arial", 18))
    lable.pack(padx=20, pady=20)

    textbox = tk.Text(root, height=2, font=("Arial", 16))
    textbox.pack(padx=10, pady=10)

    myentry = tk.Entry(root)
    myentry.pack()

    def user_click():
        logger.info("User clicked button")

    button = tk.Button(root, text="Click Me!", font=("Arial", 18), command=user_click)  # type: ignore
    button.pack(padx=10, pady=10)

    logger.debug("Entering main loop")
    root.mainloop()
    logger.debug("Exited main loop")


if __name__ == "__main__":
    main()
