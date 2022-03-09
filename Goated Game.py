from random import randint
from time import sleep
from room import Room
from item import Item
from character import Enemy, Friend

print('\n')

kitchen = Room('kitchen')
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room('ballroom')
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

dining_hall = Room('dining hall')
dining_hall.set_description("A large room with ornate golden decorations on each wall")

toilet_downstairs = Room('downstairs toilet')
toilet_downstairs.set_description('A small and cramped room filled with a nasty stench.')

toilet_upstairs = Room('upstairs toilet')
toilet_upstairs.set_description('A humid room with a broken toilet; a window is open above a huge pipe.')

corridor = Room('corridor')
corridor.set_description("A long room with many unpainted doors.")

hallway = Room('hallway')
hallway.set_description("A dim room with a large mirror.")

study = Room('study')
study.set_description("A dusty room with a single desk and cracked windows.")

bedroom_kids = Room('kids bedroom')
bedroom_kids.set_description('A bright room with rainbow wallpaper and a bunk bed.')

bedroom_master = Room('master bedroom')
bedroom_master.set_description('An old room with peeling wallpaper and a large bed.')

stairs = Room('stairs')
stairs.set_description('A creaky staircase with missing planks.')

pipe = Room('pipe')
pipe.set_description('A steep pipe that you are unable to climb back up.')

hidden_sewer = Room('hidden sewer')
hidden_sewer.set_description('An empty sewer, unused for many years; rats surround you.')

balcony = Room("balcony")
balcony.set_description("The parent's balcony; an ashtray sits on a table.")

patio = Room('patio')
patio.set_description('A stone floor with medieval railings; stairs lead to the garden.')

garden = Room('garden')
garden.set_description()

toilet_downstairs.link_room(kitchen, 'west')
kitchen.link_room(toilet_downstairs, 'east')

print('There are '+str(Room.number_of_rooms)+ ' rooms to explore.')

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness('cheese')
dining_hall.set_character(dave)

henry = Friend('Henry', 'A charming butler')
henry.set_conversation('How do you do?')
ballroom.set_character(henry)

current_room = kitchen

dead = False
while dead == False:
    print("\n")         
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("\n> ")
    
    if current_room == hidden_sewer:
        print('You are unable to do anything as the rats crawl around you.')
        command = input('\n> ')
        print('They start to wriggle under your clothes and bite you.')
        command = input('\n> ')
        print('They pull you onto the floor and completely cover you.')
        command = input('\n> ')
        print('You begin to suffocate as they climb into your mouth.')
        command = input('\n> ')
        print('You suffocate and die.')
        dead=True
        break

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print('There is no one here to talk with')
       
    elif command == "fight":

        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Hooray, you won the fight!")
                current_room.set_character(None)
            else:
                print("Oh dear, you lost the fight.")
                dead = True
        else:
            print("There is no one here to fight with")        

    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
        else:
            print("There is no one here to hug :(")

if dead=True:
    print('You lost the game')

else:
    print('Well done for making it out alive.')