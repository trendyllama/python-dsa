import tkinter as tk
import logging


def main():
    logging.basicConfig(
        filename="tk_inter_first_log.log",
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s - %(message)s",
    )

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
        logging.info("User clicked button")

    button = tk.Button(root, text="Click Me!", font=("Arial", 18), command=user_click())  # type: ignore
    button.pack(padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
