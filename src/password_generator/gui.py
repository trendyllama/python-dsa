"""
This module contains the InputBox class which creates a graphical user interface (GUI) for taking user input.

The InputBox class provides a window with a label, a text input field, and a button. When the button is clicked, the user input is retrieved and saved to a variable.

Example usage:
    input_box = InputBox("400x200", "Enter your name:")
    user_input = input_box.get_input()
"""

import logging
import tkinter as tk
from typing import Protocol

logger = logging.getLogger(__name__)

class InputBoxProtocol(Protocol):
    def __init__(self, geo: str, message: str) -> None: ...

    def init_box(self) -> None: ...

    def get_input(self) -> str: ...


class InputBox(InputBoxProtocol):
    """
    A class that creates a graphical user interface (GUI) for taking user input.

    Attributes:
        geo (str): The dimensions for the GUI window in the format "widthxheight".
        message (str): The message to display as a label in the GUI window.
        input (str): The user input retrieved from the text input field.

    Methods:
        __init__(self, geo: str, message: str) -> None:
            Initializes the InputBox object with the specified dimensions and message.

        get_input(self) -> str:
            Retrieves the user input from the text input field and returns it as a string.
    """

    def __init__(self, geo: str, message: str) -> None:
        """
        Initializes the InputBox object with the specified dimensions and message.

        Args:
            geo (str): The dimensions for the GUI window in the format "widthxheight".
            message (str): The message to display as a label in the GUI window.
        """
        logger.debug("Initializing InputBox with geo: %s and message: %s", geo, message)

        self.geo = geo
        self.message = message

        self.init_box()

    def init_box(self) -> None:
        self.root = tk.Tk()
        self.root.geometry(self.geo)

        label = tk.Label(self.root, text=self.message)
        label.config(font=("Courier", 14))
        label.pack()

        user_input = tk.Text(self.root, height=5, width=20)
        user_input.pack()

        button = tk.Button(master=self.root, text="Enter", command=self.get_input)
        button.pack()
        self.root.mainloop()

    def get_input(self) -> str:
        """
        Retrieves the user input from the text input field and returns it as a string.

        Returns:
            str: The user input as a string.
        """

        self.input = self.input.get(1.0, "end-1c")
        self.root.destroy()
        return self.input
