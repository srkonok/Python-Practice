class Employee:
    def greet(self):
        print("Employee Greet!")


class Person:
    def greet(self):
        print("Person Greet!")


class Manager1(Employee, Person):
    pass  # Employee Greet!


class Manager2(Person, Employee):
    pass  # Person Greet!


manager1 = Manager1()
manager1.greet()
manager2 = Manager2()
manager2.greet()
