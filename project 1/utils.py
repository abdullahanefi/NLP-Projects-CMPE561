import os


def listdirs(folder):
    return [d for d in os.listdir(folder)
            if os.path.isdir(os.path.join(folder, d))]


def listfiles(folder):
    return [d for d in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, d))]
