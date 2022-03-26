import copy

documents = [
            {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
            {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
            {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
            ]

directories = {
               '1': ['2207 876234', '11-2'],
               '2': ['10006'],
               '3': []
              }

def input_user():
    """
    Ф-ция пользовательского ввода, q - выход
    """
    
    while True:
        print('')
        comand = input("Введите начальную команду (q - выход, при некорректном вводе - отображение справки):")
        if comand == 'p':
            print('по команде “p” можно узнать владельца документа по его номеру')
            num_to_FIO(num_doc())
        elif comand == 's':
            print('по команде “s” можно по номеру документа узнать на какой полке он хранится')
            num_to_dir(num_doc())
        elif comand == 'l':
            print('по команде “l” можно увидеть полную информацию по всем документам')
            full_view()
        elif comand == 'as':
            print('по команде “as” можно добавить новую полку')
            add_dir(num_dir())
        elif comand == 'ds':
            print('по команде “ds” можно удалить существующую полку из данных (только если она пустая)')
            del_dir(num_dir())
        elif comand == 'ad':
            print('по команде “ad” можно добавить новый документ в данные')
            add_doc(num_dir(), num_doc())
        elif comand == 'd':
            print('по команде “d” можно удалить документ из данных')
            del_doc(num_doc())
        elif comand == 'm':
            print('по команде “m” можно переместить документ с полки на полку')
            move_doc(num_doc())
        elif comand == 'q':
            break
        else:
            print('')
            print('Некорректный ввод')
            print('')
            print('Справка по начальным командам')
            print('по команде “p” можно узнать владельца документа по его номеру')
            print('по команде “s” можно по номеру документа узнать на какой полке он хранится')
            print('по команде “l” можно увидеть полную информацию по всем документам')
            print('по команде “as” можно добавить новую полку')
            print('по команде “ds” можно удалить существующую полку из данных (только если она пустая)')
            print('по команде “ad” можно добавить новый документ в данные')
            print('по команде “d” можно удалить документ из данных')
            print('по команде “m” можно переместить документ с полки на полку')
            print('по команде “q” производиться выход из программы')
    return

def num_doc():
    number_doc = input("Введите номер документа: ")
    return number_doc

def num_dir():
    number_dir = input("Введите номер полки: ")
    return number_dir

def current_dir():
    """
    Просмотр всего перечня полок
    """
    list_dir = []
    for dir_ in directories.keys():
        list_dir.append(dir_)
    return print('Текущий перечень полок:',' '.join(list_dir))

def main():
    """
    Тело программы
    """
    
    input_user()
    print('')
    print("Произведен выход из программы.")

def num_to_FIO(number_doc):
    """
    Поиск по номеру документа владельца
    """
    result = False

    for list_doc in documents:
        num_ = list_doc.get('number')
        name_ = list_doc.get('name')
        if num_ == number_doc:
            result = True
            break

    if result == True :
        print('')
        print('Результат:')
        print(f'Владелец документа: {name_}')
    else:
        print('')
        print('Результат:')
        print('Документ не найден в базе')

def num_to_dir(number_doc):
    """
    Поиск по номеру документа полки, на которой он располагается
    """
    result = False

    for dir_, list_num_ in directories.items():
        for num_ in list_num_:
            if num_ == number_doc:
                result = True
                break
        if result == True:
            break

    if result == True :
        print('')
        print('Результат:')
        print(f'Полка с документом: {dir_}')
    else:
        print('')
        print('Результат:')
        print('Документ не найден в базе')
        
def full_view():
    """
    Просмотр всей сводки по документам
    """
    print('')
    print('Полный список документов:')
    for list_doc in documents:
        name_ = list_doc.get('name')
        type_ = list_doc.get('type')
        num_in_doc = list_doc.get('number')
        for dir_, list_num_ in directories.items():
            for num_in_dir in list_num_:
                if num_in_dir == num_in_doc:
                    print(f'ФИО: {name_} Тип документа: {type_} №: {num_in_doc} Полка №: {dir_}')

def add_dir(number_dir):
    """
    Добавление новой полки
    """
    list_dir = []
    if number_dir not in directories.keys(): 
        directories.setdefault(number_dir, [])
        current_dir()
    else:
        print('')
        print('Такая полка уже существует.', end=' ')
        current_dir()
        return

    print('')
    print('Полка добавлена.', end=' ')
    current_dir()


def del_dir(number_dir):
    """
    Удаление полки
    """
    if number_dir in directories.keys() and len(directories[number_dir]) == 0:
        directories.pop(number_dir)
        print('')
        print('Полка удалена.', end=' ')
        current_dir()
    elif number_dir in directories.keys() and len(directories[number_dir]) != 0:
            print('')
            print('Полка не пустая - ошибка удаления.', end=' ')
            current_dir()
    elif number_dir not in directories.keys():  # не использован else для наглядности логики
        print('')
        print('Такой полки не существует.', end=' ')
        current_dir()

def add_doc(dir_, num_):
    if dir_ not in directories.keys():
        print('Такой полки не существует. Добавьте полку командой as.')
        full_view()
    else:
        type_ = input("Введите тип документа:")
        name_ = input("Введите владельца документа:")
        documents.append({'type':type_, 'number':num_, 'name':name_})
        directories[dir_].append(num_)
        full_view()

def del_doc(number_doc):
    result = False
    documents_clone = copy.copy(documents)
    for list_doc in documents_clone:
        if list_doc['number'] == number_doc:
            documents.remove(list_doc)
            result = True
            break

    if result == False:
        print('Документ не найден в базе')      
    else:
        result == False
        for list_num_ in directories.values():
            for num_in_dir in list_num_:
                if num_in_dir == number_doc:
                    list_num_.remove(num_in_dir)
                    result == True
                    break
            if result == True:
                break
    full_view()

def move_doc(number_doc):
    """
    Перемещение документа
    """
    result = False
    for list_doc in documents:
        num_ = list_doc.get('number')
        if num_ == number_doc:
            result = True
            number_dir = num_dir()
            break
    if result == False:
        print('')
        print('Документ не найден в базе.')
        full_view()
    elif number_dir not in directories.keys():
        print('')
        print('Такой полки не существует.')
        current_dir()
    elif number_dir in directories.keys() and result == True:
        result = False
        for list_num_ in directories.values():
            for num_in_dir in list_num_:
                if num_in_dir == number_doc:
                    list_num_.remove(num_in_dir)
                    result == True
                    break
            if result == True:
                break
        directories[number_dir].append(number_doc)
        print('')
        print('Документ перемещен.')
        full_view()

main()
