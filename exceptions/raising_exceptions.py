# you can raise exceptions using the raise statement by providing the name of the error/exception and the
# exception object that is to be thrown

#error or exception that you can raise should be a class which directly or indirectly must be a driven class of Exception class

class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('enter something')
    if(len(text) < 3):
         raise ShortInputException(len(text), 3)
except EOFError:
    print('why did you EOF on me?')
except ShortInputException as ex:
    print('the input is {0} length, expected is atleast {1}'.format(ex.length, ex.atleast))
else:
    print('no exceptions raised')