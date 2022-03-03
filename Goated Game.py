from random import randint
from time import sleep
from shapes import Paper, Rectangle, Oval, Triangle
from room import Room

kitchen = Room('Kitchen')
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room('Ballroom')
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

dining_hall = Room('Dining Hall')
dining_hall.set_description("A large room with ornate golden decorations on each wall")

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')

dining_hall.get_details()