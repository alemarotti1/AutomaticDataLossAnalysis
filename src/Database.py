from genericpath import exists
from re import I
import DirectoryManager
import pathlib
import os
import json
import PIL
import numpy as np

class Database:
    def __init__(self, path, model_name):
        state, exists = self.get_project_data(path, model_name)
        self.change_level = 0
        self.path = path
        self.database = state
        if(exists):
            pass
        

    def get_database(self):
        return self.database

    def update_database(self, id, state, evaluation):
        #for every file in the database whose name is id update the state and evaluation
        map(lambda x: x if x["file"] != id else {"file": x["file"], "evaluation": evaluation, "state": state}, self.database["file_list"])


        #self.database["file_list"] [id]["evaluation"] = evaluation
        #self.database["file_list"][id]["state"] = state
        self.change_level += 1
        return self.change_level

    def get_entry(id):
        return id

    def get_change_level(self):
        return self.change_level

    def changed_instance():
        return []
    
    def get_project_data(self, path, model):
        exists = False
        print("Getting project data")
        print(path)
        file = (path/("state.json"))
        
        project = path.parent.parent.name
        if(not os.path.isfile(file)):
            file = open(file, "w+")
            #trasform from json to list
            list = DirectoryManager.get_list_from_project(project)
            json_list = {'number_of_rights': 0,'number_of_wrongs': 0, 'number_of_unknowns': 0 ,'file_list': []}
            number_of_unknown = 0
            for x in list:
                #create dict
                dict = {"file": x, "evaluation": -1, "state": "unknown"}
                #write dict to file
                json_list["file_list"].append(dict)
                number_of_unknown += 1
            json_list["number_of_unknowns"] = number_of_unknown
            file.write(json.dumps(json_list))

        else:
            file_json = open(file, "r+")
            #trasform from json to list
            json_list = json.load(file_json)
            exists = True
        return json_list, exists