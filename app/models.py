class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


class Document:
    def __init__(self, id, filename, filepath):
        self.id = id
        self.filename = filename
        self.filepath = filepath