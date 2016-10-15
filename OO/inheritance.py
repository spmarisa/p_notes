# one way of reuse of code is done by inheritance mechanism
# inheritance can be best imagined as implementing a type and subtype relationship between classes
class SchoolMember:

    def __int__(self, name, age):
        self.name = name
        self.age = age

        print('initialized SchoolMember {0}'.format(self.name))

    def tell(self):
        print('Name:"{0}" Age:"{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('initialized teacher: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        # print('Marks: "{0:d}"'.format(self.marks)


# t = Teacher('Mrs. Shrividya', 40, 30000)

# s = Student('Swaroop', 25, 75)

# print()

# members = [t, s]
# for member in members:
#     member.tell()