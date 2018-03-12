import sys
from notebook import Notebook, Note

class Menu:
    """Display a menu and respond to choices"""
    def __init__(self):
        self.notebook=Notebook()
        self.choices={
            "1":self.show_notes,
            "2":self.search_notes,
            "3":self.modify_note,
            "4":self.add_note,
            "5":self.quit
        }
    def display_menu(self):
        print("""
        **********************
        Notebook Menu
        1. Show all notes
        2. Search notes
        3. Modify note
        4. Add note
        5. Quit
        **********************
        """)
    def run(self):
        """display the menu and respond to choices"""
        while True:
            self.display_menu()
            choice=input("Enter an option: \n")
            action=self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice \n".format(choice))

    def show_notes(self,notes=None):
        """print notes in the list"""
        if not notes:
            notes=self.notebook.notes
        for note in notes:
            print("""
______________________________________________________
{0}: {1}\n{2}
______________________________________________________""".format(note.id,note.tags,note.memo))

    def search_notes(self):
        """search for notes by filter"""
        filter=input("Search for: ")
        notes=self.notebook.search(filter)
        print("Searched results for \"{0}\"".format(filter))
        self.show_notes(notes)

    def add_note(self):
        memo=input("Enter a memo: \n")
        self.notebook.new_note(memo)
        print("Note has been added.")
    def modify_note(self):
        id=input("Enter a note id: \n")
        memo=input("Enter a new memo: \n")
        tags=input("Enter new tags: \n")
        if memo:
            self.notebook.modify_memo(id,memo)
        if tags:
            self.notebook.modify_tags(id,tags)

    def quit(self):
        print("Thank you for using your notebook!")
        sys.exit(0)
if __name__=="__main__":
    Menu().run()