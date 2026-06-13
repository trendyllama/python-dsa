from ctypes import CDLL
import logging


if __name__ == "__main__":
    # Configure logging and load the shared library
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    cfile = CDLL("./cfile.so")

    # Call the C function
    result = cfile.add(5, 3)
    logger.info("Result from C function: %s", result)
