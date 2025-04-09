
# User-Defined Exception
class InvalidRollNumberError(Exception):
    def __init__(self,msg):
        self.msg = msg     # msg = "ROll number should not be negative

class InvalidNameError(Exception):
    def __init__(self,msg):
        self.msg = msg

class InvalidPercentageError(Exception):
    def __init__(self,msg):
        self.msg = msg