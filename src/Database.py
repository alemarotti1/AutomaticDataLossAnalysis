

database = [0,1,2]
change_level = 0

def get_database():
    return database

def update_database(id, state):
    #database[id] = state
    change_level += 1
    return change_level

def get_entry(id):
    return id

def get_change_level():
    return change_level

def changed_instance():
    return []

