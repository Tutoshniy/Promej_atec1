def function_select():
    func_select = input("Выберите режим работы:\
          1. Добавить заметку\
          2. Редактировать заметку\
          3. Удалить заметку\
          4. Вывести заметки\
          5. Вывести содержимое заметки\
          6. Выход ")
    if not func_select.isdigit() and int(func_select) < 1 and int(func_select) > 6:
        print("Введено недопустимое значение. Попробуйте ещё раз.")
        func_select = function_select()
    else:
        print()
    return int(func_select)
