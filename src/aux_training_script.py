from ModelController import ModelController
import csv
import random
import pathlib
import PIL
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf

mc = ModelController()

mc.activate_project("zhangai")

print(mc.active_project)

mc.activate_model("model0")

def train(X, Y):
    #convert the lists to numpy arrays
    X = np.array(X)
    Y = np.array(Y)

    #split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    #get only the first 10 images and labels
    print("initiating training")
    print(X_train.shape)
    print(Y_train.shape)
    #train the model
    mc.update_model_bulk(X_train, Y_train)

    #evaluate the model
    mc.model.modelImage1.model.evaluate(X_test, Y_test)



#open the csv file at "../database/database_test.csv"
with open("../database/database_test.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    
    #randomize the order of the rows
    rows = list(reader)
    random.shuffle(rows)

    X = []
    Y = []

    images_added = 0
    runs = 0

    #separate the last 30 images from the rest
    test_rows = rows[-30:]
    train_rows = rows[:-30]


    #for each row
    for row in train_rows:
        print("row: " + str(runs*10+images_added)+ " of " + str(len(rows)))
        if images_added >= 10:
            train(X, Y)
            X = []
            Y = []
            images_added = 0
            runs += 1
        #get the project
        project = row[0]
        #get the image
        image = row[1]
        #get the label
        label = row[2]

        #get the image path
        image_path = pathlib.Path("../projetos") / project / "dataloss"
        path = sorted((image_path).glob("*/"+image+"*.*"))

        image_after = PIL.Image.open(path[0])
        #scale the image to half the size
        image_after = image_after.resize((int(image_after.width//2), int(image_after.height//2)), PIL.Image.ANTIALIAS)
        image_after_table = np.array(image_after)
        image_before = PIL.Image.open(path[1])
        image_before = image_before.resize((int(image_before.width//2), int(image_before.height//2)), PIL.Image.ANTIALIAS)
        image_before_table = np.array(image_before)

        
        #diff between the images
        diff = image_after_table - image_before_table
        
        #remove the alpha channel
        diff = diff[:,:,:3]

        #normalize the images
        new_image = diff/255

        X.append(new_image)
        if label == "False Positive":
            Y.append([0,1])
        else:
            Y.append([1,0])
        images_added += 1
        

    hits = 0
    total = 0
    for row in test_rows:
        #get the project
        project = row[0]
        #get the image
        image = row[1]
        #get the label
        label = row[2]

        #get the image path
        image_path = pathlib.Path("../projetos") / project / "dataloss"
        path = sorted((image_path).glob("*/"+image+"*.*"))

        image_after = PIL.Image.open(path[0])
        #scale the image to half the size
        image_after = image_after.resize((int(image_after.width//2), int(image_after.height//2)), PIL.Image.ANTIALIAS)
        image_after_table = np.array(image_after)
        image_before = PIL.Image.open(path[1])
        image_before = image_before.resize((int(image_before.width//2), int(image_before.height//2)), PIL.Image.ANTIALIAS)
        image_before_table = np.array(image_before)

        
        #diff between the images
        diff = image_after_table - image_before_table
        
        #remove the alpha channel
        diff = diff[:,:,:3]

        #normalize the images
        new_image = diff/255
        result = ""
        prediction = mc.model.predict(new_image)
        print(prediction)
        if prediction[0]<prediction[1]:
            result = "False Positive"
        else:
            result = "True Positive"
        if result == label:
            hits += 1
        total += 1
    print("hits: "+str(hits))
    print("total: "+str(total))
    print("accuracy: "+str(hits/total))

    # save mc.model.modelImage1.model to disk
    mc.model.modelImage1.model.save("../models/model0.h5")


