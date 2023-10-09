def read_notes():
    notes = {}
    file = open("notes.txt", "r")
    for line in file.readlines():
        elements = line.split(":")
        notes[elements[0]] = elements[1]
    return notes