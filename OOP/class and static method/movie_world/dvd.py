from calendar import month_name


class DVD:
    def __init__(self, name, id_num, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id_num
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_num, name, date, age_restriction):
        d, m, y = [int(x) for x in date.split(".")]

        return cls(name, id_num, y, month_name[m], age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"