from course import Course
from student import Student

class Quiz:
    def __init__(self):
        self.__count = 1

    def increment(self):
        self.__count += 1

    def get_count(self):
        return self.__count

class School:
    def __init__(self, name: str):
        self.name = name 
        self.students = [] 
        self.courses = [] 
        self.next_student_id = 1  

    def add_course(self, course: Course):
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student: Student):
        if student not in self.students:
            student.set_id(self.next_student_id)
            self.students.append(student)
            self.next_student_id += 1

    def add_student_grade(self, student: Student, course: Course, grade: int):
        if student in self.students and course in self.courses:
            student.add_student_grade(course, grade)
            course.add_student_grade(student, grade)

    def get_students(self):
        return self.students

    def get_courses(self):
        return self.courses

    def get_students_ordered_by_average_grade(self):
        return sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)

    def __repr__(self):
        return f"Kool({self.name})"

if __name__ == '__main__':
    school = School("Tallinna Kool")

    course1 = Course("MAtemaatika")
    course2 = Course("Füüsika")

    school.add_course(course1)
    school.add_course(course2)

    student1 = Student("Markus")
    student2 = Student("Anna")

    school.add_student(student1)
    school.add_student(student2)

    school.add_student_grade(student1, course1, 4)
    school.add_student_grade(student1, course2, 5)
    school.add_student_grade(student2, course1, 3)

    students_ordered = school.get_students_ordered_by_average_grade()
    for student in students_ordered:
        print(f"{student.name}: {student.get_average_grade()}")