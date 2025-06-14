def conversion(units: str, temp: float):
    if units == "F" or units == "Fahrenheit":
        c = (temp - 32) * (5 / 9)
        if c == 0:
            print("Freezing point for water!")
        elif c == 100:
            print("Boiling point for water!")
        return print(f"The temperature in Celcius is {c}")
    elif units == "C" or units == "Celcius":
        f = (temp * (9 / 5)) + 32
        if f == 32:
            print("Freezing point for water!")
        elif f == 212:
            print("Boiling point for water!")
        return print(f"The temperature in Fahrenheit is {f}")
    else:
        print("Input F or C, your units aren't right!")


def main():
    print("What units are you conveting from?")
    units = input("Type Fahrenheit or Celcius: ")
    temp = float(input("Type the temperature in those units: "))

    conversion(units, temp)


if __name__ == "__main__":
    main()
