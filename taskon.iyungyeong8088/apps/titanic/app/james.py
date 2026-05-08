from fastapi import FastAPI

from titanic.app.rose import Rose
from titanic.app.walter import Walter


app = FastAPI(title="Titanic (James)")


class James:
    def __init__(self):
        pass


    def get_data(self):
        w = Walter()
        return w.get_data()

    def get_count(self):
        w = Walter()
        return w.get_count()
        
    def get_survived(self):
        w = Walter()
        return w.get_survived()

    def has_decision_tree_model(self):
        rose = Rose()
        return rose.has_saved_model()
