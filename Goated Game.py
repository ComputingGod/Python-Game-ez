from random import randint
from time import sleep
from shapes import Paper, Rectangle, Oval, Triangle
from room import Room

kitchen = Room('Kitchen')
kitchen.set_description("A dank and dirty room buzzing with flies")
kitchen.get_description()
ballroom = Room('Ballroom')
dining_hall = Room('Dining Hall')