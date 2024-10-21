"""Encapsulation exercise."""

class Student:
    """
    Represent student with name, id and status.

    :name: str The name of the student
    :id: int The ID of the student
    :status: str The status of the student (default is: "Active").
    """
    

    def __init__(self, name: str, student_id: int):
        """
        Initializes a Student object with a name and UID.
        
        :name: str The name of the student.
        :student_id: int The UID of the student.
        """
        self.__name = name
        self.__id = student_id
        self.__status = "Active"

    def get_id(self) -> int:
        """
        Returns the UID of the student.

        :Returns: int UID of the student.
        """
        return self.__id

    def set_name(self, name: str):
        """
        Sets a new name for the student.
        
        :name: str New name of the student.
        """
        self.__name = name

    def get_name(self) -> str:
        """
        Returns the current name of the student.
        
        :Returns: str Returns the current name of the student.
        """
        return self.__name

    def set_status(self, status: str):
        """
        Sets a new status for the student if its valid status.
        
        :status: str The new status for the student ID.
        """
        valid_statuses = {"Active", "Expelled", "Finished", "Inactive"}
        if status in valid_statuses:
            self.__status = status

    def get_status(self) -> str:
        """
        :Returns: str The current status of the student.
        """
        return self.__status

Test = Student("MArkus", 123)
print(Test.get_status())