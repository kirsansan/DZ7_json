# This is a simple Python script. ;-)
# HomeWork from lesson 7.2. Python 20 groupe
# writted by Kirill.S

# from basic_word import BasicWord
# from player import Player
from jdata.utils import  load_from_json_file, get_profession_by_title, get_student_by_pk, check_fitness
from config.config import FILE_FOR_STUDENTS, FILE_FOR_PROFESSIONS
from my_new_input.my_input import InputAndCheckString


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # init variables block
    students_dict: dict = load_from_json_file(FILE_FOR_STUDENTS)
    professions_data: dict = load_from_json_file(FILE_FOR_PROFESSIONS)
    professions_options: dict = [item['title'] for item in professions_data]

    input_and_check: InputAndCheckString = InputAndCheckString()  # string for work with user
    input_and_check.input_while_correct("Введите номер студента >")

    number_of_student: str = input_and_check.input_string
    # print(input_and_check.input_string)
    if number_of_student.isdigit() and int(number_of_student) in range(0, len(students_dict)):
        one_student_data = get_student_by_pk(int(number_of_student), students_dict)
    else:
        print("Нет такого студента!")
        quit(101)   # HR must reread CVV

    input_and_check.input_while_correct(f"Выберите специальность для оценки "
                                        f"студента {one_student_data['full_name']} >")
    what_is_level_hr_need: str = input_and_check.input_string

    # print("prof data:    ", professions_data)
    # print("prof_options: ", professions_options)
    if what_is_level_hr_need in professions_options:
        skills_for_hr: list = get_profession_by_title(what_is_level_hr_need, professions_data)
    else:
        print("увольте HR-а, У нас нет такой специальности")
        quit(102) # HR must be fire
    #print(what_is_a_skills4need)

    i_kwon_all_about_this_student: dict = check_fitness(one_student_data, skills_for_hr)
    print("Пригодность: ", i_know_all_about_this_student['fit_percent'])
    print(one_student_data['full_name'], "знает", ', '.join(i_kwon_all_about_this_student['has']))
    print(one_student_data['full_name'], "не знает", ', '.join(i_kwon_all_about_this_student['lacks']))

    if True:
        print("Таких не берут в космонавты (с) ")
    else:
        print("Если вы проверяете этот код - как получить доступ к урокам с 10 по 13?")

# this is end of this short history
