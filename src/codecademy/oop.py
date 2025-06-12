
class School:
    def __init__(self, name, level, numberofStudents):
        self.name = name
        self.level = level
        self.numberofStudents = numberofStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberofStudents(self):
        return self.numberofStudents

    def set_numberofStudents(self, num):
        self.numberofStudents = num

    def __repr__(self):
        return (
            "A "
            + str(self.level)
            + " school named "
            + str(self.name)
            + " with "
            + str(self.numberofStudents)
            + " students"
        )


s = School("Hill", "High", 100)

# print(s)


class PrimarySchool(School):
    def __init__(self, name, numberofStudents, pickupPolicy):
        super().__init__(name, "primary", numberofStudents)
        self.pickupPolicy = pickupPolicy

    def get_pp(self):
        return self.pickupPolicy

    def __repr__(self):
        return super().__repr__()


p = PrimarySchool("Wyndcroft", 500, "Parents only")

# print(p)


class HighSchool(School):
    def __init__(self, name, numberofStudents, sportsTeams):
        super().__init__(name, "High", numberofStudents)
        self.sportsTeams = sportsTeams

    def get_st(self):
        return self.sportsTeams

    def __repr__(self):
        return "We offer {} as extra ciricular sports".format(self.sportsTeams)


h = HighSchool("Lawrenceville", 100, ["Soccer", "Track", "Hockey"])

print(h)