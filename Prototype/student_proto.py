from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Student(Prototype):
    def __init__(self, name, age, gender, school_id, grade, school_email, school_phone, school_address):
        self.name = name
        self.age = age
        self.gender = gender
        self.school_id = school_id
        self.grade = grade
        self.school_email = school_email
        self.school_phone = school_phone
        self.school_address = school_address

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"School ID: {self.school_id}\n"
            f"Grade: {self.grade}\n"
            f"School Email: {self.school_email}\n"
            f"School Phone: {self.school_phone}\n"
            f"School Address: {self.school_address}\n"
        )

    def clone(self):
        return copy.deepcopy(self)

student1 = Student(
    name="Ana Rodríguez",
    age=17,
    gender="Female",
    school_id="HS2025-045",
    grade="12th",
    school_email="ana.rodriguez@highschool.edu",
    school_phone="(664) 123-4567",
    school_address="123 High School Ave, Tijuana, BC"
)

print(student1)

juan = student1.clone()

juan.name = "Juan Perez"

print(juan)
