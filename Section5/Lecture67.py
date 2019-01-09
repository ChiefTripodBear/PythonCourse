
class CustomError(ValueError) : 
    def __init__(self, message, code):
        super().__init__(f'Error Code {code}: {message}')
        self.code = code

raise CustomError('You have an error.', 500)