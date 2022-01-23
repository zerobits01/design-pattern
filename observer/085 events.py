class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


# observer is good for when we need to be aware
# when something happens in the system
# now adays we can use something like async events


# e.g we need to change something based on changes on other parts

# thats one of the most important programming points
# we have to learn event based

# most important thing here is to know
# what should we pass as an event
# sending the event generator, source, timestamp, log and etc etc


# how to handle remove and unsubscribe it
# we can combine it with command and have roleback

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f'A doctor has been called to {address}')

if __name__ == '__main__':
    person = Person('Sherlock', '221B Baker St')

    person.falls_ill.append(lambda name, addr: print(f'{name} is ill'))

    person.falls_ill.append(call_doctor)

    person.catch_a_cold()

    # and you can remove subscriptions too
    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()