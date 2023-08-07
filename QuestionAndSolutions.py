import examSystemData


class QuestionData:
    def __init__(self, obj: examSystemData.Exam):
        self.question_database = obj.question_list

    def add_question(self, list_of_values: list):
        empty_question = examSystemData.Question()
        for key in empty_question.question_info.keys():
            empty_question.question_info[key] = list_of_values[0]
            list_of_values = list_of_values[1:]
        self.question_database.append(empty_question)

    def edit_question(self, v_num: int, v_key='', v_value=''):
        obj = self.question_database[v_num - 1]
        for key in obj.question_info.keys():
            if key == v_key:
                obj.question_info[key] = v_value

    def print_sorted_question_list_by_diff(self):
        list_of_dict = []
        for m_dict in self.question_database:
            list_of_dict.append(m_dict.question_info)
        print(sorted(list_of_dict, key=lambda i: i['Difficulity']))

    def print_filtered_question_list(self, v_key='', v_value=''):
        for i in range(0, len(self.question_database)):
            obj = self.question_database
            for key, value in obj[i].question_info.items():
                if key == v_key and value == v_value:
                    examSystemData.Question.print_question_info(self.question_database[i])
                    continue


class SolutionData:
    def __init__(self):
        self.solution_list = []

    def add_sol(self, sol=''):
        self.solution_list.append(sol)

    def edit_sol(self, question=0, new_sol=''):
        self.solution_list[question - 1] = new_sol
