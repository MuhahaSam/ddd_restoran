class EmailExistException(Exception):
    def __init__(self):
        self.message = "email exist"
        super().__init__(self.message)
