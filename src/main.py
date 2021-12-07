import threading
#import concurrent.futures
import Database
#import ModelController

#import ModelController
import Gui



def main():
    #mc = ModelController()
    #modelThread = threading.Thread(target=mc.startModel, args=(), daemon=True)
    #modelThread.start()

    #guiThread = threading.Thread(target=Gui.startWebView, args=(), daemon=True)
    #guiThread.start()
    
    print(Database.get_database())
    
    #modelThread.join()
    #guiThread.join()
    




#create a main that will run the program
if __name__ == '__main__':
    main()