class Menu:
    """
    Example:
    >>> brunch_items = {
    ...     "pancakes": 7.50,
    ...     "waffles": 9.00,
    ...     "burger": 11.00,
    ...     "home fries": 4.50,
    ...     "coffee": 1.50,
    ...     "espresso": 3.00,
    ...     "tea": 1.00,
    ...     "mimosa": 10.50,
    ...     "orange juice": 3.50,
    ... }
    >>> brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)
    >>> brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"])
    13.5
    """

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return (
            "The "
            + self.name
            + " menu is availble from "
            + str(self.start_time)
            + " to "
            + str(self.end_time)
            + "."
        )

    def calculate_bill(self, purchased_items):
        bill = 0
        for item in purchased_items:
            if item in self.items:
                bill += self.items[item]
        return bill


class Franchise:
    """

    Example:
    >>> brunch_items = {
    ...     "pancakes": 7.50,
    ...     "waffles": 9.00,
    ...     "burger": 11.00,
    ...     "home fries": 4.50,
    ...     "coffee": 1.50,
    ...     "espresso": 3.00,
    ...     "tea": 1.00,
    ...     "mimosa": 10.50,
    ...     "orange juice": 3.50,
    ... }
    >>> brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)
    >>> flagship_store = Franchise("1232 West End Road", [brunch_menu])
    >>> flagship_store.available_menus(1200)
    [The Brunch menu is availble from 1100 to 1600.]
    >>> new_installment = Franchise("12 East Mulberry Street", [brunch_menu])
    >>> new_installment.available_menus(1200)
    [The Brunch menu is availble from 1100 to 1600.]
    """

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus


class Business:
    """
    Example:



    """

    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


def main():
    # Brunch
    brunch_items = {
        "pancakes": 7.50,
        "waffles": 9.00,
        "burger": 11.00,
        "home fries": 4.50,
        "coffee": 1.50,
        "espresso": 3.00,
        "tea": 1.00,
        "mimosa": 10.50,
        "orange juice": 3.50,
    }

    brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)

    print(brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"]))

    # Early Bird
    early_bird_items = {
        "salumeria plate": 8.00,
        "salad and breadsticks (serves 2, no refills)": 14.00,
        "pizza with quattro formaggi": 9.00,
        "duck ragu": 17.50,
        "mushroom ravioli (vegan)": 13.50,
        "coffee": 1.50,
        "espresso": 3.00,
    }

    early_bird_menu = Menu("Early Bird", early_bird_items, 1500, 1800)

    print(
        early_bird_menu.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"])
    )

    # Dinner
    dinner_items = {
        "crostini with eggplant caponata": 13.00,
        "ceaser salad": 16.00,
        "pizza with quattro formaggi": 11.00,
        "duck ragu": 19.50,
        "mushroom ravioli (vegan)": 13.50,
        "coffee": 2.00,
        "espresso": 3.00,
    }

    dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

    # Kids
    kids_items = {
        "chicken nuggets": 6.50,
        "fusilli with wild mushrooms": 12.00,
        "apple juice": 3.00,
    }

    kids_menu = Menu("Kids", kids_items, 1100, 2100)

    # Take a' Arepa Menue
    arepas_menu = {
        "arepa pabellon": 7.00,
        "pernil arepa": 8.50,
        "guayanes arepa": 8.00,
        "jamon arepa": 7.50,
    }

    # Flagship Store
    flagship_store = Franchise(
        "1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
    )

    new_installment = Franchise(
        "12 East Mulberry Street",
        [brunch_menu, early_bird_menu, dinner_menu, kids_menu],
    )

    arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

    # print(flagship_store.available_menus(1900))

    # Basta Fazoolin Business
    Basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])


    # Take a' Arepa Business
    Arepa = Business("Take a' Arepa", arepas_place)

    print(Arepa.franchises)


if __name__ == "__main__":
    main()
