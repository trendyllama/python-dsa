""" """


class School:
    """

    Example:
    >>> s = School("Hill", "High", 100)
    >>> s.name
    'Hill'
    >>> s.level
    'High'
    >>> s.numberofStudents
    100
    >>> s.__repr__()
    'A High school named Hill with 100 students'
    """

    def __init__(self, name, level, number_of_students):
        self.name = name
        self.level = level
        self.numberofStudents = number_of_students

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberofStudents} students"


class PrimarySchool(School):
    """
    Example:
    >>> p = PrimarySchool("Wyndcroft", 500, "Parents only")
    >>> p.name
    'Wyndcroft'
    >>> p.level
    'primary'
    >>> p.numberofStudents
    500
    """

    def __init__(self, name, num_students, pickup_policy):
        super().__init__(name, "primary", num_students)
        self.pickupPolicy = pickup_policy

    def get_pp(self):
        return self.pickupPolicy

    def __repr__(self):
        return super().__repr__()


class HighSchool(School):
    """

    Example:
    >>> h = HighSchool("Lawrenceville", 100, ["Soccer", "Track", "Hockey"])
    >>> h.name
    'Lawrenceville'
    >>> h.level
    'High'
    >>> h.numberofStudents
    100
    >>> h.sportsTeams
    ['Soccer', 'Track', 'Hockey']
    >>> h.__repr__()
    "We offer ['Soccer', 'Track', 'Hockey'] as extra ciricular sports"
    """

    def __init__(self, name, number_of_students, sports_teams):
        super().__init__(name, "High", number_of_students)
        self.sportsTeams = sports_teams

    def get_st(self):
        return self.sportsTeams

    def __repr__(self):
        return f"We offer {self.sportsTeams} as extra ciricular sports"
