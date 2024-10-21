"""Simple class."""

class Student:
    """
    Class for representing the student.
    
    
    :param name: str The name of the student.
    :param finished: bool Indicating if the student has finished their studies.
    """
    
    def __init__(self, name: str):
        """
        Makes all of the necessary attributes for the student object.

        :name: str The name of the student.
        """
        self.name = name
        self.finished = False
