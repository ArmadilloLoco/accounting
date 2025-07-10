'''В модуле people.py функция get_employees.'''
from datetime import datetime

def get_employees():
   return 'Get employees. Date: %s' % datetime.now().strftime('%d-%m-%Y')