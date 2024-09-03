from class_variable_vs_instance_varibale import RateOfInterest

class ParentClass:

    def __init__(self):
        print('Parent class instance')

    def parent_method(self):
        print('Parent method')

class ChildClass(ParentClass):

    pass

parent_class = ParentClass()
parent_class.parent_method()

child_class = ChildClass()
child_class.parent_method()

class Student(RateOfInterest):
    interest = 0.05

student = Student('Kabir', 40000)
student.calculate_interest()