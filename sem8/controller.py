import model as m
import view as v

def start():
    options = [find, position, salary, new_person, del_person, update, export_json, export_csv, exit_of_program]
    return options[v.show_menu() - 1]()

def find():
    return v.info(m.find_person(v.find()))

def position():
    return m.filter_doljnost(v.doljnost())

def salary():
    return m.filter_salary(v.salary())

def new_person():
    res = m.add_member(v.add_new_personal())
    return v.info(res)

def del_person():

    return 0

def update():

    return 0

def export_json():
    # передавать словарь
    return 0

def export_csv():

    return 0

def exit_of_program():

    return 0

