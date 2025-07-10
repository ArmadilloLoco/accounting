'''основной модуль для запуска программы'''

import application.salary as s # custom
import application.db.people as p # custom
import numpy as np 
import pprint as pp


def analyze_salaries(num_employees: int) -> dict: # 4.
    '''Генерирует и анализирует данные о зарплатах сотрудников.'''
    
    # Генерация случайных зарплат
    salaries = np.random.randint(30000, 150000, size=num_employees)
    # Расчёт статистики
    result = {
        'salaries': salaries.tolist() ,
        'average': float(np.mean(salaries)),
        'max': float(np.max(salaries)),
        'min': float(np.min(salaries)),
    }
    return result

if __name__ == '__main__':
    # 2. Импортировать функции в модуль main.py 
    print(s.calculate_salary()) # 3. При вызове функций модуля main.py выводить текущую дату.
    print(p.get_employees())

    print('Salary statistics:')
    pp.pprint( analyze_salaries(5)) # 4. Найти интересный для себя пакет на pypi и в файле requirements.txt указать его с актуальной версией. 

