import datetime
last_id=0
class Note:
    """Represent a note in the notebook"""
    def __init__(self,memo,tags=''):
        """init a note with  memo and optional space separated tag"""
        self.memo=memo
        self.tags=tags
        self.creation_date=datetime.date.today()
        global last_id
        last_id+=1
        self.id=last_id

    def match(self,filter):
        """determine if there is note matches the filter"""
        return filter in self.memo or filter in self.tags

class Notebook:
    """Represent a collection of notes that can
    be tagged, modified and searched"""
    def __init__(self):
        '''init a notebook with an empty list'''
        self.notes=[]

    def new_note(self,memo,tags=''):
        """add a note"""
        self.notes.append(Note(memo,tags))

    def modify_memo(self,note_id,memo):
        """modify the memo"""
        self._find_note(note_id).memo=memo

    def modify_tags(self, note_id, tags):
        """modify the tags"""
        self._find_note(note_id).tags=tags

    def search(self,filter):
        """search with filter"""
        return [note for note in self.notes if note.match(filter)]

    def _find_note(self,note_id):
        for note in self.notes:
            if note.id==note_id:
                return note
        return None



