import model
import view

# Создаем файл с номерами тлф
def button_click_create():
    model.create_data()
    view.create_view()

# Получаем данные (номера тлф)
def button_click_import():
    model.data_coming()
    view.data_coming_view(model.data_coming())

# Создаем тлф. книгу и выгружаем в файл
def button_click_export():
    model.export_data()
    view.import_view()