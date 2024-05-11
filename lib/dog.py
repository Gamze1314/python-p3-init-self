#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed


new_dog = Dog("chula")
print(new_dog)
print(new_dog.name)
print(new_dog.breed)

new_dog.breed = "terrier"

print(new_dog.breed)