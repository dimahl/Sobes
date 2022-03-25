import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from random import randint

def create_date(N, year0, month0, day0):
    """Функция создает N меток дата_время, year0, month0, day0 - начальная дата """
    
    d0 = datetime(year0, month0, day0)
    random_date_time = []

    for i in range(N):
        week = randint(0, 52)
        day = randint(0, 28) 
        hour = randint(0, 23)
        minute = randint(0, 59)
        delta = timedelta(weeks=week, days=day, hours=hour, minutes=minute)
        random_date_time.append(d0 + delta)
    return random_date_time

N1 = 100 # Количество строк в таблице 1
N3 = 100000 # Количество строк в таблице 3

current_balance = np.round(abs(70 + 300 * np.random.randn(N1)), 2)
date_add = create_date(N1, 2018, 3, 8)
age = np.random.randint(18, 70, size=N1)
city = ['Москва'] * N1
last_session = create_date(N1, 2022, 2, 3)
current_tarif = np.random.randint(2, size=N1)

data1 = {'Текущий баланс':current_balance, 'Дата добавления':date_add, 
        'Возраст':age, 'Город проживания': city, 'Временная метка последней активности':last_session,
       'Активный тариф': current_tarif}
table_1 = pd.DataFrame(data=data1) # Таблица 1 – Абоненты/Пользователи

table_2 = pd.DataFrame(data={'Название':['БезПереплат', 'Максимум'], 'Дата начала действия':['2020-01-01', '2021-11-15'],
                            'Дата конца действия':['2021-01-01', '2030-01-01'], 'Объем минут':[300, 800],
                            'Объем смс':[150, 500], 'Объем трафика (мб)':[1024, 16384]})

type_uslugi = ['звонок', 'смс', 'трафик']
label_time = create_date(N3, 2022, 1, 3)
id_user = np.random.randint(0, N1, size=N3)
usluga = [type_uslugi[np.random.randint(3)] for i in range(N3)]
volume_spent_usluga = np.random.randint(1, 30, size=N3)
data3 = {'Метка времени':label_time, 'id абонента':id_user, 
        'Тип услуги':usluga, 'Объем затраченных единиция': volume_spent_usluga}

table_3 = pd.DataFrame(data=data3) # Таблица 3 – События использования услуг
table_3['Метка времени'] = table_3['Метка времени'].dt.date # convert datetime to date

# Делаю сводную таблицу по колонке Тип услуги, т.о. получаю агрегированую таблицу по юзерам и дням 
report = pd.pivot_table(table_3,
               index=["id абонента", "Метка времени"],
               columns=["Тип услуги"],
               values=['Объем затраченных единиция'],
               aggfunc=[np.sum],
               fill_value=0)
report.columns = ['звонок', 'смс', 'трафик'] #Привожу в соотвутствие имена колонок
report.reset_index(inplace=True) #Привожу в соотвутствие колонки
report.head(5)

  