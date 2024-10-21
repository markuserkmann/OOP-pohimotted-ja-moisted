"""Constructor exercise."""

class Empty:
    """An empty class without constructor."""
    pass


class Person:
    """Represent person with firstname, lastname and age."""
    def __init__(self):
        """
        Constructs a Person object with default values or given values.
        
        firstname: str - First name.
        lastname: str - Last name.
        age: int - Age.
        """
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""
    def __init__(self, firstname: str, lastname: str, age: int):
        """
        Constructs a Student object with given values.
        
        firstname: str - First name.
        lastname: str - Last name.
        age: int - Age
        """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    empty_obj = Empty()
    print(empty_obj)

    p1 = Person()
    p1.firstname = "Anna"
    p1.lastname = "Karutina"
    p1.age = 25

    p2 = Person()
    p2.firstname = "Boberino"
    p2.lastname = "Erkmann"
    p2.age = 30

    p3 = Person()
    p3.firstname = "Carol"
    p3.lastname = "Must"
    p3.age = 28

    print(f"{p1.firstname} {p1.lastname}, Age: {p1.age}")
    print(f"{p2.firstname} {p2.lastname}, Age: {p2.age}")
    print(f"{p3.firstname} {p3.lastname}, Age: {p3.age}")

    s1 = Student("Debug", "Tarantel", 22)
    s2 = Student("Test", "Koer", 21)
    s3 = Student("Test", "Ahv", 23)

    print(f"{s1.firstname} {s1.lastname}, Age: {s1.age}")
    print(f"{s2.firstname} {s2.lastname}, Age: {s2.age}")
    print(f"{s3.firstname} {s3.lastname}, Age: {s3.age}")