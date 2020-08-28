import mlflow

def set_note(note):
    mlflow.set_tag('mlflow.note.content', note)