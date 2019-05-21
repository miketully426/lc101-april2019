class Student:

    def __init__(self, student_id, first_name, last_name, birthdate):
       self.student_id = student_id
       self.first_name = first_name
       self.last_name = last_name
       self.birthdate = birthdate
       self.grades = {}

    def get_first_name(self):
        return self.first_name

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def get_gpa(self):
        total = 0
        for grade in self.grades.values():
            total += grade
        return total/len(self.grades)

    def __str__(self):
        return "Name: " + self.first_name + " " + self.last_name

def main():
    bob = Student(4, "Bob", "Boberson", "11/23/89")
    print(bob.get_first_name())

    bob.add_grade("LC 101", 4)
    bob.add_grade("CHM 103", 0)

    print(bob)

if __name__ == "__main__":
    main()