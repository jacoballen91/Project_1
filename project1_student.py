import csv
"""Write header"""
with open('grades.csv', 'w', newline='') as output_csv:
    contents = csv.writer(output_csv)
    contents.writerow(['Name', 'Attempt 1', 'Attempt 2', 'Attempt 3', 'Attempt4', 'Final'])



class Student:

    def __init__(self, name: str) -> None:
        """
        Initializes base values for student
        """
        self.student_name = self.check_name(name)


    def check_name(self, name: str) -> str:
        """
        Validate student name, simply ensuring there is an entry
        :return: student name
        """
        student = name.strip()
        if len(student) > 0:
            return student
        else:
            raise NameError

    def check_attempts(self, attempts: str) -> int:
        """
        Validate attempt entry, checking that the entry is numeric and between 1 and 4
        :return: number of attempts.
        """
        num_attempts = int(attempts)
        if 1 <= num_attempts <= 4:
            return num_attempts
        else:
            raise TypeError

    def get_grade(self, attempt1: str = 0, attempt2: str = 0, attempt3: str = 0, attempt4: str = 0) -> int:
        """
        Attempts are initialized as 0, and modified by GUI entry
        Check that attempt scores are numeric and between 0 and 1
        Write grades to grades.csv and calculate final score.
        """
        attempt1 = int(attempt1)
        attempt2 = int(attempt2)
        attempt3 = int(attempt3)
        attempt4 = int(attempt4)
        grades_list = [attempt1, attempt2, attempt3, attempt4]
        if max(grades_list) > 100 or min(grades_list) < 0:
            raise TypeError

        else:
            final_grade = max(grades_list)
            with open('grades.csv', 'a', newline='') as output_csv:
                contents = csv.writer(output_csv)
                contents.writerow([self.student_name, attempt1, attempt2, attempt3, attempt4, final_grade])
            return final_grade
