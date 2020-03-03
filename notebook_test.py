from notebook import Note, Notebook
from menu import Menu

menu = Menu()
print('Exploring menu:')
print('Menu attributes:')
print(dir(menu))

print()
print('Exploring classes Notebook and Note:')
print('Note1: Hello it is me!!!')
print('Note2: Here me again.')
print('Note3: Hello everyone in the world.')

notee = Note('Hello it is me!!!','me')
noteee = Note('Here me again', 'hi!')
note = Note('Hello everyone in the world.', 'world')
notebook = Notebook()

print('Type of the note, the dictionary of first note, first note attributes: ')
print(type(notee))
print(notee.__dict__)
print(dir(notee))
note_match = notee.match('my note')
note_match2 = notee.match('Hello')
print('first note match function result(word: my note):', note_match)
print('first note match function result(word: Hello): ', note_match2 )

notebook.new_note(notee.memo, notee.tags) #сreating a new note
notebook.new_note(noteee.memo, noteee.tags)
notebook.new_note(note.memo, note.tags)
print('All notes in the notebook:')
for note in notebook.notes:
    print(note.__dict__)

print('Notebook notes: ')
print(notebook.notes)

print('Find the first note:')
find = notebook._find_note(notebook.notes[0].id)
print(find.memo)

print('Example of using modifying memo, tags function(changing one memo and one tag):')
notebook.modify_memo(notebook.notes[0].id, 'Good bye')
notebook.modify_tags(notebook.notes[1].id, 'you with me')
for note in notebook.notes:
    print('note memo: ', note.memo)
    print('note tag: ', note.tags)

print('Example of using search function(word: Here):')
for note in notebook.search('Here'):
    print(note.memo)

print()
print('Exploring classes using dir and isinstance: ')

print('Note attributes and methods: ', dir(note))
print('Notebook attributes and methods:', dir(notebook))

print('note is Note: ', isinstance(note, Note))
print('notebook is Notebook: ', isinstance(notebook, Notebook))

print('note.id is int: ', isinstance(note.id, int))
print('note.memo is str: ', isinstance(note.memo, str))

print('note.id attributes and methods: ',dir(note.id))
print('note.memo attributes and methods: ', dir(note.memo))
print('note.match attributes and methods:', dir(note.match))
print('notebook.__init__ attributes and methods:', dir(notebook.__init__))
print('notebook.new_note attributes and methods:', dir(notebook.new_note))

print('Exploring notebook and notes as objects and their methods: ')
print('notebook is object: ', isinstance(notebook, object))
print('note is object: ', isinstance(note, object))
print('notebook.__str__ is str: ', isinstance(notebook.__str__, str))
print('notebook.__str__ is object: ', isinstance(notebook.__str__, object))
print('notebook.__init__ is object: ', isinstance(notebook.__init__, object))
print('notebook.new_note is object: ', isinstance(notebook.new_note, object))
