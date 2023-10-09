def printTitleNotes(notes):
    print("Все заметки: ")
    if notes == {}:
        print("Пока что заметок нет")
    for i in list(notes):
        print(i)
    print()