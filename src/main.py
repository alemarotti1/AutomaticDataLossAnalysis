import threading
import eel
#import concurrent.futures
import Database
from ModelController import ModelController

#import ModelController
import Gui

mc = ModelController()

@eel.expose
def get_projects():
    return mc.get_projects()

@eel.expose
def get_project_data(project):
    return mc.get_project_data(project)

@eel.expose
def receive_feedback(img_name,feedback):
    return mc.get_feedback(img_name, feedback)

def main():
    # mc = ModelController()
    # modelThread = threading.Thread(target=mc.startModel, args=(), daemon=True)
    # modelThread.start()

    guiThread = threading.Thread(target=Gui.startWebView, args=(), daemon=True)
    guiThread.start()
    
    print(Database.get_database())
    
    #modelThread.join()
    guiThread.join()




#a main that will run the program
if __name__ == '__main__':
    main()