
class Student:
    def __init__(self, name, student_id, grade_level):
        self.name = name
        self.student_id = student_id
        self.grade_level = grade_level
        self.subjects = {}

    def add_subject(self, subject_name, score):
        self.subjects[subject_name] = score

    def calculate_average(self):
        total = sum(self.subjects.values())
        return total / len(self.subjects)

    def get_grade(self, score):
        if score >= 90:
            return "A+"
        elif score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "F"

    def has_passed(self):
        return all(score >= 50 for score in self.subjects.values())

    def generate_report(self):
        average = self.calculate_average()
        final_grade = self.get_grade(average)
        status = "PASS" if self.has_passed() else "FAIL"

        print("\n=== Report Card ===")
        print(f"Name       : {self.name}")
        print(f"ID         : {self.student_id}")
        print(f"Class      : {self.grade_level}")
        print(f"Average    : {average:.2f}")
        print(f"Grade      : {final_grade}")
        print(f"Result     : {status}\n")

        print("Subject-wise Breakdown:")
        print("------------------------")
        for subject, score in self.subjects.items():
            grade = self.get_grade(score)
            result = "Pass" if score >= 50 else "Fail"
            print(f"{subject:<15} | {score:>5} | Grade: {grade} | {result}")

def main():
    print("=== Student Grade Calculator (OOP Version) ===\n")

    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    grade_level = input("Enter class/grade level: ")

    student = Student(name, student_id, grade_level)

    num_subjects = int(input("\nEnter number of subjects: "))
    for i in range(num_subjects):
        subject = input(f"Subject {i + 1} name: ")
        score = float(input(f"Marks in {subject}: "))
        student.add_subject(subject, score)

    student.generate_report()

if __name__ == "__main__":
    main()
