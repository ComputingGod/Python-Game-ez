from random import randint
from time import sleep
from room import Room
from item import Item
from character import Enemy, Friend

print('\n')
enemies=[]

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

hidden_pipe1 = Room('hidden pipe')
hidden_pipe1.set_description('A hidden steep pipe that leads to an old sewer.')

hidden_pipe2 = Room('further down the hidden pipe')
hidden_pipe2.set_description('You are unable to climb back up the pipe. See what lays ahead!')

sewer = Room('sewer')
sewer.set_description('An empty sewer, unused for many years; rats surround you.')

balcony = Room("balcony")
balcony.set_description("The parent's balcony; an ashtray sits on a table.")

patio = Room('patio')
patio.set_description('A stone floor with medieval railings; stairs lead to the garden.')

garden = Room('garden')
garden.set_description('Overgrown with vines and shrubbery.')

doorstep = Room('doorstep')
doorstep.set_description('A stone step in front of a giant wooden door.')

porch = Room('porch')
porch.set_description('A boot room full of cobwebs.')

gate = Room('gate')
gate.set_description('A tall and rusty metal gate.')

toilet_downstairs.link_room(kitchen, 'west')
kitchen.link_room(toilet_downstairs, 'east')

patio.link_room(kitchen, 'north')
kitchen.link_room(patio, 'south')

garden.link_room(patio, 'east')
patio.link_room(garden, 'west')

garden.link_room(doorstep, 'north')
doorstep.link_room(garden, 'south')

doorstep.link_room(porch, 'east')
porch.link_room(doorstep, 'west')

hallway.link_room(porch, 'west')
porch.link_room(hallway, 'east')

ballroom.link_room(hallway, 'south')
hallway.link_room(ballroom, 'north')

dining_hall.link_room(hallway, 'north')
hallway.link_room(dining_hall, 'south')

hallway.link_room(corridor, 'east')
corridor.link_room(hallway, 'west')

corridor.link_room(kitchen, 'south')
kitchen.link_room(corridor, 'north')

corridor.link_room(study, 'east')
study.link_room(corridor, 'west')

corridor.link_room(stairs, 'north')
stairs.link_room(corridor, 'south')

stairs.link_room(bedroom_kids, 'east')
bedroom_kids.link_room(stairs, 'west')

stairs.link_room(toilet_upstairs, 'west')
toilet_upstairs.link_room(stairs, 'east')

toilet_upstairs.link_room(hidden_pipe1, 'north')
hidden_pipe1.link_room(toilet_upstairs, 'south')

hidden_pipe1.link_room(hidden_pipe2, 'north')

hidden_pipe2.link_room(sewer, 'north')

stairs.link_room(bedroom_master, 'north')
bedroom_master.link_room(stairs, 'south')

bedroom_master.link_room(balcony, 'north')
balcony.link_room(bedroom_master, 'south')


print('There are '+str(Room.number_of_rooms)+ ' rooms to explore.')

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness('cheese')
dining_hall.set_character(dave)
enemies.append(dave)

henry = Friend('Henry', 'A charming butler')
henry.set_conversation('How do you do?')
ballroom.set_character(henry)

current_room = doorstep

dead = False
while dead == False:
    print("\n")         
    current_room.get_details()
    if current_room == gate:
        print('You found the exit!')
        break

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("\n> ")
    
    if current_room == sewer:
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
                enemies.remove(inhabitant)
                if len(enemies)>1:
                    print('You have '+len(enemies)+' enemies remaining.')
                elif len(enemies)==1:
                    print('You have '+len(enemies)+' enemies remaining.')
                elif len(enemies)==0:
                    print('You have defeated all the enemies, the exit has now been unlocked, go and find it!')
                    doorstep.link_room(gate, 'west')
                    
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

if dead==True:
    print('You lost the game')

else:
    print('Well done for making it out alive.')