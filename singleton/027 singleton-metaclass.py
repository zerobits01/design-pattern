class Singleton(type):
    """ Metaclass that creates a Singleton base type when called. """
    _instances = {} 
    
    # its an outsider way this is a singleton ref for all
    # classes which gonna use this design pattern mode

    def __call__(cls, *args, **kwargs):
        print("call is called")
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, **kwargs)
        return cls._instances[cls]

# metaclass is act as an class decorator mode
class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')


if __name__ == '__main__':
    Database() # the metaclas call will be called in this mode
    d1 = Database() # the metaclas call will be called also in this mode
    d2 = Database() # the metaclas call will be called also in this mode
    print(d1 == d2)

'''
__new__ creates the instance of a Class, you use it when you need to control the creation of a new instance.

we can use __new__ when we gonna handle the problem in insider mode


__init__ is used to initialize the instance variables once the instance is created by __new__.

__call__ is like a function call operator. Once you implement __call__ in your Class,
'''
# https://devnote.in/difference-between-__init__-__call__-and-__new__/#:~:text=__CALL__()%20is%20used%20for,called%20by%20a%20callable%20object.


