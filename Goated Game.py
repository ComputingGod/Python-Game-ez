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

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

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

    command = input("> ")
    
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
       
    elif command == "fight":

        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Hooray, you won the fight!")
                current_room.set_character(None)
            else:
                print("Oh dear, you lost the fight.")
                print("That's the end of the game")
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
            