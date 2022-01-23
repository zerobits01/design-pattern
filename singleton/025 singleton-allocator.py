import random

class Database:
    initialized = False

    # this method of defining singleton class
    # is the insiders mode which we handle the created instance
    # inside the class itself

    def __init__(self):
        # self.id = random.randint(1,101)
        # print('Generated an id of ', self.id)
        # print('Loading database from file')
        # in these kind of classes we shouldnt have init
        # we may get True for d1 == d2 but the init will be run differently
        # so we have to only write __new__
        pass

    _instance = None

    def __new__(cls, *args, **kwargs):
        # its a specific class method in python
        # it takes cls so its @classmethod
        if not cls._instance:
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)

        return cls._instance


database = Database()

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()

    print(d1.id, d2.id)
    print(d1 == d2)
    print(database == d1)

# e.g at work we can overwrite redis_client such this