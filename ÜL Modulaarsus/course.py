"""Course class with name and grades."""

from student import Student

class Course:
    def __init__(self, name: str):
        self.name = name or "Puudub"
        self.grades = []

    def add_student_grade(self, student: Student, grade: int):
        for existing_student, _ in self.grades:
            if existing_student == student:
                return
        if isinstance(grade, int) and 0 <= grade <= 100:
            self.grades.append((student, grade))
        else:
            raise ValueError("Hinne peab olema täisarv 0-100")

    def get_grades(self):
        return self.grades

    def get_average_grade(self):
        if not self.grades:
            return -1
        total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)

    def __repr__(self):
        return self.name
