

# defining the magic decorator
def singleton(class_):
    ###########################################
    # this part is the same for all classes and
    # all intiations, its an outsider way of handling
    instances = {}
    print(f'instances are: {instances}')
    print(f'class is: {class_}')
    ###########################################
    def get_instance(*args, **kwargs):
        # if it doesnt exist return it
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        # here it has been created if it didnt exist or 
        # it returns if it did exist before without re-initial
        print(f'instances after change are: {instances}')
        return instances[class_]
    ###########################################
    return get_instance

# each class which is in singleton mode can only intiailized one time

@singleton # the signleton itself will be run here
class Database:
    def __init__(self):
        print('Loading database')

    # __new__ is another way but the init will be run many times

if __name__ == '__main__':
    d1 = Database() # insider function get_instance will be run here and it will be added after first call
    d2 = Database() # insider function get_instance will be run here and it will be get instead recreation
    # !! loading the database is only once
    print(d1 == d2)
    pass

'''
instances are: {}
class is: <class '__main__.Database'>
Loading database
instances after change are: {<class '__main__.Database'>: <__main__.Database object at 0x7fcc8a4b2f10>}
instances after change are: {<class '__main__.Database'>: <__main__.Database object at 0x7fcc8a4b2f10>}
True
'''