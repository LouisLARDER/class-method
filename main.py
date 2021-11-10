class Student:
    gender = 'Female'

    def __init__(self, scores = []):
        self.scores = scores

    def avg(self):
        return round(sum(self.scores) / len(self.scores))

    @staticmethod
    def notice():
        return "exams next week"

    @classmethod
    def what_genders(cls):
        return f"i am {cls.gender}"

print(Student.what_genders())