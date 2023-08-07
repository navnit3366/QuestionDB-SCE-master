import examSystemData


def get_exam_info(obj: examSystemData.Exam):
    with open('Exams.txt') as f:
        line = f.read().split()
    obj.exam_date = line[0]
    obj.exam_semester = line[1]


def get_question_info(obj: examSystemData.Exam):
    with open('Questions.txt') as f:
        for line in f:
            if not line.strip():
                break
            line = line.split()
            empty_question = examSystemData.Question()
            for key in empty_question.question_info.keys():
                empty_question.question_info[key] = line[0]
                line = line[1:]
            obj.question_list.append(empty_question)


def get_course_info(obj_course: examSystemData.Course, obj_exam: examSystemData.Exam):
    with open('Courses.txt') as f:
        line = f.read().split()
    obj_course.course_name = line[0]
    obj_course.lecturer_name = line[1]
    obj_course.year_of_course = line[2]
    obj_course.exam = obj_exam


def get_department_info(obj_course: examSystemData.Course, obj_department: examSystemData.Department):
    with open('Departments.txt') as f:
        line = f.read().split()
    obj_department.dep_name = line[0]
    obj_department.coordinator_name = line[1]
    obj_department.course = obj_course
