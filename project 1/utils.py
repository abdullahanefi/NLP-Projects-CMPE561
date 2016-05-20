import os


def list_dirs(folder):
    return [d for d in os.listdir(folder)
            if os.path.isdir(os.path.join(folder, d))]


def list_files(folder):
    return [d for d in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, d))]
