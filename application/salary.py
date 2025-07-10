'''В модуле salary.py функция calculate_salary'''
from datetime import datetime

def calculate_salary():
    return 'Calculate salary. Date: %s' % datetime.now().strftime('%d-%m-%Y')
