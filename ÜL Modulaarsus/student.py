"""Student class with student name and grades."""

class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades = []
        self.id = None

    def __repr__(self) -> str:
        return self.name

    def set_id(self, id: int):
        if self.id is None:
            self.id = id

    def get_id(self) -> int:
        return self.id

    def get_grades(self):
        return self.grades

    def get_average_grade(self):
        if not self.grades:
            return -1 
        total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)

    def add_student_grade(self, course: "Course", grade: int):
        if isinstance(grade, int) and 0 <= grade <= 100:
            self.grades.append((course, grade))
            course.add_student_grade(self, grade)
        else:
            raise ValueError("Hinne peab olema 0-100 vahel")
