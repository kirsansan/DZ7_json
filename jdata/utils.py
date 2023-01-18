""" utils for working with json-format file"""

import json


def load_from_json_file(filename: str ='./students.json') -> dict:
    """ load any information from json-format file and return it"""
    # response = urllib.request.urlopen(external_adr)
    # data = json.loads(response.read())
    # random_num_from_data: int = random.randint(0, len(data) - 1 )

    # load from file
    with open(filename, 'r', encoding='utf-8') as fh:  # open file
        data = json.load(fh)  # load data
    # print(data)

    # deshifrate data and put to my structure

    # in first version just return all data
    return data

def get_student_by_pk(pk: int, data: dict = {} ) -> dict:
    """ return dict by the number of record"""
    for challanger in data:
        if challanger['pk'] == pk:
            return challanger
    return None

def get_profession_by_title(title: str, data: dict = {}) -> list:
    """ return list of strings by the string of title"""
    for challanger in data:
        if challanger['title'] == title:
            return challanger['skills']
    print("kak ya suda popal?")
    return None

def check_fitness(student: dict, profession: list) -> dict:
    """ compare student by professions
        and calculate percents of skill which have this student in list of profession
        "has": ["Python", "Linux"],
        "lacks": ["Docker, SQL"],
        "fit_percent": 50
    """
    has: list[str:] = []
    lacks: list[str:] = []

    # print("vot skills nashego studenta: ", student['skills'])
    # print("a vot professii:             ", profession)
    has = list(set(student['skills']) & set(profession))
    lacks = list(set(profession) - set(student['skills']))
    fit_percent: int = round(100*len(has)/len(profession), 0)
    # [has.append(search_prof) for search_prof in profession if student['skills'] in profession['skills'] ]
    return {'has': has, 'lacks': lacks, "fit_percent": int(fit_percent)}

# def load_random_word() -> BasicWord:
#     """ create one BasicWord fill it from external data and return it
#         request data from jsonkeeper
#         be careful with kaspersky and other useless firewalls !
#         alternatively use npoint.io resurse
#     """
#     #external_adr: str = "https://jsonkeeper.com/b/P3L7"  # it doesn't work =(
#     external_adr: str = "https://api.npoint.io/8e92a5832c382022b229"  # it worked!!
#
#     # don't delete this codes - it will be needed if I win against "VERIFY_SERTIFICATE" error
#     #external_adr = "http://maps.googleapis.com/maps/api/geocode/json?address=google"
#     #response = urllib.request.urlopen(external_adr,  context=ssl.create_default_context(cafile=certifi.where()))
#     # ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())
#
#     response = urllib.request.urlopen(external_adr)
#
#     data = json.loads(response.read())
#     random_num_from_data: int = random.randint(0, len(data) - 1 )
#
#     # fill word for return
#     new_word4created: BasicWord = BasicWord(data[random_num_from_data]['word'], data[random_num_from_data]['subwords'])
#
#     return new_word4created
#
# # need write exeption handler, but it not describe in SOW


# this block for a self-test
if __name__ == '__main__':
    students_data = load_from_json_file('./students.json')
    profession_data = load_from_json_file('./professions.json')
    print(students_data)
    print(profession_data)

    one_student = get_student_by_pk(1, students_data)
    print("Student: ",one_student)
    skills_for_search = get_profession_by_title('Backend', profession_data)
    print("Prof: ", skills_for_search)

    some_result = check_fitness(one_student, skills_for_search)
    print(some_result)

