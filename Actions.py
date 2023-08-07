import examSystemData
import UserData
import QuestionAndSolutions
import logger


def print_coordinator_menu():
    print('1 - add a lecturer to the system\n2 - edit lecturer info')
    print('3 - add a solution\n4 - add a question')
    print('5 - edit a solution')
    print_leturer_menu()


def print_leturer_menu():
    print('6 - edit a question')
    print_student_menu()


def print_student_menu():
    print('7 - display question by Difficulity')
    print('8 - filter the questions shown by criteria')
    print('Press 0 to exit')


def interface(user, obj: examSystemData.Exam):
    logger.logger.info('Entered User Interface')
    obj_user_data = UserData.UserData()
    obj_questions = QuestionAndSolutions.QuestionData(obj)
    obj_solutions = QuestionAndSolutions.SolutionData()
    permmision = 0  # 1 - C, 2 - L, 3 - C
    print('You can :')
    if user == 'Coordinator':
        print_coordinator_menu()
        logger.logger.info('Entered Coordinator User Interface')
        permmision = 1
    elif user == 'Lecturer':
        print_leturer_menu()
        logger.logger.info('Entered Lecturer User Interface')
        permmision = 2
    elif user == 'Student':
        print_student_menu()
        logger.logger.info('Entered Student User Interface')
        permmision = 3

    while True:
        choice = input()
        if choice == '1' and permmision == 1:
            logger.logger.info('Entered Main Menu')
            lecturer_first_name, lecturer_last_name = input(
                'enter lecturer first name + last name with a whitespace between : ').split()
            obj_user_data.add_lecturer(lecturer_first_name, lecturer_last_name)
            logger.logger.info('Added Lecturer To User System')

        elif choice == '2' and permmision == 1:
            lecturer_first_name, lecturer_name_change = input(
                'enter lecturer first name + the change with a whitespace between : ').split()
            obj_user_data.edit_lecturer_info(lecturer_first_name, lecturer_name_change)
            logger.logger.info('Edited Lecturer`s info In User System')

        elif choice == '3' and permmision == 1:
            obj_solutions.add_sol(input('Add A solution : '))
            logger.logger.info('Added Solution To DataBase')

        elif choice == '4' and permmision == 1:
            list_of_values = input('enter with - Difficulity, Topic, sub_topic, Code, Format : ').split()
            obj_questions.add_question(list_of_values)
            logger.logger.info('Added Question To DataBase')

        elif choice == '5' and permmision == 1:
            question = int(input("What answer would you want to edit?"))
            new_sol = input('Enter Your Edit')
            obj_solutions.edit_sol(question, new_sol)
            logger.logger.info('Edited Solution In DataBase')

        elif choice == '6' and (permmision == 1 or permmision == 2):
            key = input('enter what you want to change, Difficulity, Topic, sub_topic, Code, Format : ')
            num = int(input('Enter questions number : '))
            value = input('enter your new value : ')
            obj_questions.edit_question(num, key, value)
            logger.logger.info('Edited Question In DataBase')

        elif choice == '7' and (permmision == 1 or permmision == 2 or permmision == 3):
            obj_questions.print_sorted_question_list_by_diff()
            logger.logger.info('Printed Question List By Diff')

        elif choice == '8' and (permmision == 1 or permmision == 2 or permmision == 3):
            key = input('enter your filter-by-criteria : ')
            value = input('enter your filter-by-value : ')
            obj_questions.print_filtered_question_list(key, value)
            logger.logger.info('Printed Question List By Criteria')

        elif choice == '0':
            logger.logger.info('Exited User Interface')
            break

        else:
            print('Invalid Choice, Try Again')
            logger.logger.warning('Bad Input')
