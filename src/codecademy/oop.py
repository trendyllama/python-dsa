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

    def __init__(self, name, level, numberofStudents):
        self.name = name
        self.level = level
        self.numberofStudents = numberofStudents

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberofStudents} students"


class PrimarySchool(School):
    '''
    Example:
    >>> p = PrimarySchool("Wyndcroft", 500, "Parents only")
    >>> p.name
    'Wyndcroft'
    >>> p.level
    'primary'
    >>> p.numberofStudents
    500
    '''
    def __init__(self, name, numberofStudents, pickupPolicy):
        super().__init__(name, "primary", numberofStudents)
        self.pickupPolicy = pickupPolicy

    def get_pp(self):
        return self.pickupPolicy

    def __repr__(self):
        return super().__repr__()


class HighSchool(School):
    '''

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
    '''
    def __init__(self, name, numberofStudents, sportsTeams):
        super().__init__(name, "High", numberofStudents)
        self.sportsTeams = sportsTeams

    def get_st(self):
        return self.sportsTeams

    def __repr__(self):
        return "We offer {} as extra ciricular sports".format(self.sportsTeams)
