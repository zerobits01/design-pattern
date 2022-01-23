class Person:
    def __init__(self):
        print('Creating an instance of Person')

        # getting all these params from this initiator is crazy
        # we have to create different builders for getting all related
        # information in a fluent way, this is when we use return self as well

        # address
        self.street_address = None
        self.postcode = None
        self.city = None

        # employment info
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        # allways it will be run on print method
        return f'Address: {self.street_address}, {self.postcode}, {self.city}\n' +\
            f'Employed at {self.company_name} as a {self.postcode} earning {self.annual_income}'


class PersonBuilder:  # facade
    
    # def __init__(self, person=Person()) -> None:
    #     self.person = person

    # another way is like upper but that way is not good
    # it will keeps a copy of the latter created person 
    
    def __init__(self, person=None):
        if person is None:
            self.person = Person()
        else:
            self.person = person

    @property
    def lives(self):
        # this gonna be a property this is not a function to call
        # we access this by .lives not .lives()
        # when we call this we are working with our address builder
        # we can work on all address related info
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        # the same for lives but here its about job
        return PersonJobBuilder(self.person)

    def build(self):
        # after using .lives and then .works we call this and
        # we can use the created person
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == '__main__':
    pb = PersonBuilder() # this will be initiated with empty person
    p = pb\
        .lives\
            .at('123 London Road')\
            .in_city('London')\
            .with_postcode('SW12BC')\
        .works\
            .at('Fabrikam')\
            .as_a('Engineer')\
            .earning(123000)\
        .build()
    print('p1 is:', p)
    person2 = PersonBuilder().build()
    print('p2 is:', person2)


'''
# output with first constructor:

Creating an instance of Person
p1 is: Address: 123 London Road, SW12BC, London
Employed at Fabrikam as a SW12BC earning 123000
p2 is: Address: 123 London Road, SW12BC, London
Employed at Fabrikam as a SW12BC earning 123000


# output with second constructor:

Creating an instance of Person
p1 is: Address: 123 London Road, SW12BC, London
Employed at Fabrikam as a SW12BC earning 123000
Creating an instance of Person
p2 is: Address: None, None, None
Employed at None as a None earning None

'''