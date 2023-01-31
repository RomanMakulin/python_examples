# data = open('traning/tran01/file.txt', 'r')
# result_list = list()
# for line in data.readlines(): # Считываем файл по строкам (но там будет \n)
#     result_list.append(tuple(line.split('\n')[0].split(';'))) # Убираем \n, определяем каждый элемент с разделителем ';' и кладем необходимые данные в картежи
# print(result_list)

from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route('/')
def main():
    with open('file.txt', 'r', encoding='utf-8') as file:
        result_list = list()
        for line in file.readlines():
            result_list.append(tuple(line.split('\n')[0].split(';')))
    return render_template('base.html', name=result_list)

if __name__ == '__main__':
    app.run()