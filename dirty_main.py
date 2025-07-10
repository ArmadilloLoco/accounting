'''импортировать все функции с помощью конструкции from package.module import * '''

from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    # Создать рядом с файлом main.py модуль dirty_main.py и импортировать все функции с помощью конструкции.
    print(calculate_salary())
    print(get_employees())