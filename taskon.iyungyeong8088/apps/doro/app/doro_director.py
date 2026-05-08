from doro.app.doro_reader import DoroReader


class DoroDirector:
    def __init__(self):
        pass

    def get_data(self):
        reader = DoroReader()
        return reader.get_data()