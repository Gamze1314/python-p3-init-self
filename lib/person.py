#!/usr/bin/env python3

class Person:
    # init method runs whenever we instantiate a new Person object. 
    def __init__(self, name):
        self.name = name  #binding name argument to self 


new_person = Person("John")
print(new_person)
        
