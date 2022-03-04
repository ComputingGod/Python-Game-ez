from random import randint
from time import sleep
from room import Room
from item import Item
from character import Character
from character import Enemy

print('\n')

kitchen = Room('kitchen')
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room('ballroom')
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

dining_hall = Room('dining hall')
dining_hall.set_description("A large room with ornate golden decorations on each wall")

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness('cheese')

current_room = kitchen

dave.describe()
dave.talk()

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)

while True:
    print('\n')
    current_room.get_details()
    command=input('> ')
    current_room = current_room.move(command)