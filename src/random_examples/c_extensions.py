from ctypes import CDLL

if __name__ == "__main__":
    # Load the shared library
    cfile = CDLL("./cfile.so")

    # Call the C function
    result = cfile.add(5, 3)
    print("Result from C function:", result)
