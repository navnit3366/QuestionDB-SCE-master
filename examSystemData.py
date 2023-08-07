class Question:
    def __init__(self):
        self.question_info = {'Difficulity': '', 'Topic': '', 'sub_topic': '', 'Code': '', 'Format': ''}

    def print_question_info(self):
        for k, v in self.question_info.items():
            print(f'{k} : {v}')


class Exam:
    def __init__(self, exam_date='', semester=''):
        self.exam_date = exam_date
        self.exam_semester = semester
        self.question_list = []


class Course:
    def __init__(self, course_name='', lecturer_name='', year_of_course=''):
        self.course_name = course_name
        self.lecturer_name = lecturer_name
        self.year_of_course = year_of_course
        self.exam = Exam()


class Department:
    def __init__(self, dep_name='', coordinator_name=''):
        self.dep_name = dep_name
        self.coordinator_name = coordinator_name
        self.course = Course()
