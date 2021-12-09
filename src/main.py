import threading
import eel
#import concurrent.futures
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

@eel.expose
def activate_project(project):
    var = mc.activate_project(project)
    return var

@eel.expose
def get_images(image_name):
    return mc.get_images(image_name)

@eel.expose
def create_model():
    return mc.create_model()

@eel.expose
def get_model_data(model):
    return mc.get_model_data(model)

@eel.expose
def get_models():
    return mc.get_models()


def main():
    # mc = ModelController()
    # modelThread = threading.Thread(target=mc.startModel, args=(), daemon=True)
    # modelThread.start()

    guiThread = threading.Thread(target=Gui.startWebView, args=(), daemon=True)
    guiThread.start()
    
    
    #modelThread.join()
    guiThread.join()




#a main that will run the program
if __name__ == '__main__':
    main()