def save_notes(notes):
    file = open("notes.txt", "w")
    for i in list(notes):
        file.write(f"{i}:{notes[i]}\n")
    file.close()