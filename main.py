#1-misol
class Student:
    def __init__(self, name, age, grade, password):
        self.name = name
        self.age = age
        self._grade = grade
        self.__password = password

    def study(self, hours):
        self._grade += hours

    def check_password(self, pw):
        return self.__password == pw

    def info(self):
        return f"{self.name} Grade:{self._grade}"


ali = Student("Ali", 20, 70, "1234")


ali.study(10)
print(ali.info())
print(ali.check_password("1234"))
print(ali.check_password("0000"))
