from notebook import Note, Notebook
n=Notebook()

n.new_note("hello world")

#unit testing
assert len(n.notes) == 1, "note creating error"
assert n.notes[0].id==1, "note id assignment error"


