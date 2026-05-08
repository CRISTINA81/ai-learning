import os

notes_file = "notes.txt"

def show_menu():
    print("===================")
    print("     NOTES APP     ")
    print("===================")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Delete a note")
    print("4. Quit")

def add_note():
    note = input("Enter your note: ")
    with open(notes_file, "a") as f:
        f.write(note + "\n")
    print("Note Saved! ✅")

def view_notes():
    with open(notes_file, "r") as f:
        notes = f.readlines()
    for note in notes:
        print(note)

def del_note():
    with open(notes_file, "r") as f:
        notes = f.readlines()
    for i, note in enumerate(notes, 1):
        print(f"{i}.{note}" )
    choice = int(input("Which note do you want to delete? "))
    notes.pop(choice -1)
    with open(notes_file, "w") as f:
        notes = f.writelines(notes)
    print("Note Deleted!  🗑️")



while True:
    show_menu()
    choice = input("pick a number 1-4: ")
    if choice not in ["1","2","3","4"]:
        print("Pick a number between 1 and 4!")
    elif choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        del_note()
    elif choice == "4":
        print("Goodbye! 👋")
        break

