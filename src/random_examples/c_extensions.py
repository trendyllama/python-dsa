from ctypes import CDLL


if __name__ == "__main__":
    # Load the shared library
    cfile = CDLL("./cfile.so")
