
class Tracking51Exception(Exception):
    def __init__(self, message):
        super(Tracking51Exception, self).__init__()
        self.message = message

    def __str__(self):
        return '{}: {}'.format(self.__class__.__name__, self.message)