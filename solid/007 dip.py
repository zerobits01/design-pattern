from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser: 
    # this is a kinda interface for finding all childs
    # this way we can change the low level implementation
    @abstractmethod
    def find_all_children_of(self, name): pass


class Relationships(RelationshipBrowser):  # low-level
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.PARENT, parent)
        )
            
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    # dependency on a low-level module directly
    # bad because strongly dependent on e.g. storage type

    # def __init__(self, relationships):
    #     # high-level: find all of john's children
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f'John has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# low-level module
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)

'''
working exactly on a tuple gonna be a crazy job!
what if we change the data-type! then we should overwrite
whatever we wrote for this!!! this is realy bad

we have to write modules as abstract as possible this way
if we change the implementation of somewhere we wont see any change
on other parts 

e.g we can write proxy or interface classes for accessing each part
this way we can change inner part without change of outside
'''

'''
better method is:
we write some interfaces and now we can overwrite the interface
but we can add new interfaces which they are more efficent
then till we change other places we can support the older mode
sometimes some interfaces can be un-efficient
'''