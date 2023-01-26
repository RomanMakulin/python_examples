import model as m
import view as v

def start():
    options = [find, position, salary, new_person, del_person, update, export_json, export_csv, exit_of_program]
    return options[v.show_menu() - 1]()

def find():
    return m.find_person(v.find())

def position():
    return m.filter_doljnost(v.doljnost())

def salary():
    return m.filter_salary(v.salary())

def new_person():
    res = m.add_member(v.add_new_personal())
    return v.info(res)

def del_person():
    return m.del_member(v.delete())

def update():
    return m.update_person(v.upd())

def export_json():
    return m.export(v.exporting())

def export_csv():
    return m.export(v.exporting())

def exit_of_program():
    return m.exit(v.prog_out())