import control
import interface
import data_save
import data_read
print("Вас приветствует приложение 'заметки'")
notes = data_read.read_notes()
power_on = True
while power_on:
    func_select = control.function_select()
    if func_select == 1:
        title = input("Введите название заметки: ")
        body = input("Введите содержимое заметки: ")
        notes[title] = body
        data_save.save_notes(notes)
    if func_select == 2:
        interface.printTitleNotes(notes)
        title_redact = input("Введите название редактируемой заметки: ")
        if title_redact not in list(notes):
            print("Извините, такой заметки нет")
            continue
        body_redact = input("Введите новый текст для заметки: ")
        notes[title_redact] = body_redact
    if func_select == 3:
        interface.printTitleNotes(notes)
        notes_delete = input("Введите заметку, которую хотите удалить: ")
        if notes_delete not in list(notes):
            print("Извините, такой заметки нет")
            continue
        del notes[notes_delete]
    if func_select == 4:
        interface.printTitleNotes(notes)
    if func_select == 5:
        interface.printTitleNotes(notes)
        notes_body_read = input("Введите ту заметку, содержание которой хотите просмотреть: ")
        if notes_body_read not in list(notes):
            print("Извините, такой заметки нет")
            continue
        print(notes[notes_body_read])
    if func_select == 6:
        print("Спасибо, что воспользовались заметками. До свидания.")
        print()
        power_on = False
