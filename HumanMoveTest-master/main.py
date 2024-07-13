
class Student:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def walk(self):
        self.distance += 5
        #    print(self.distance)
        return self.distance

    def run(self):
        self.distance += 10
    #    print(self.distance)
        return self.distance

    def __str__(self):
        return self.name

x = 0
student_1 = Student('Vasya',x)

y = 15
student_2 = Student('Petya',y)

x = 0
student_3 = Student('Kolya',x)
y = 15
student_4 = Student('Sasha',y)