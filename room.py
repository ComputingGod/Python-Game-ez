class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
    
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description
    
    def describe(self):
        print(self.description)