import random
import shutil
import os

from utils import list_files, list_dirs


def pre_process(input_path='./raw_texts/',
                output_path='./preprocessed_texts/'):
    directories = list_dirs(input_path)
    # print (directories)

    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    os.makedirs(output_path)
    training_path = os.path.join(output_path, "training")
    test_path = os.path.join(output_path, "test")

    os.makedirs(training_path)
    os.makedirs(test_path)

    # num_documents_by_author = {}

    for author_name in directories:
        os.makedirs(os.path.join(test_path, author_name))
        os.makedirs(os.path.join(training_path, author_name))

        author_path = os.path.join(input_path, author_name)
        files_of_author = list_files(author_path)

        # num_documents_by_author[author_name] = len(files_of_author)

        test_size = len(files_of_author) * 4 / 10

        for i in range(0, int(test_size)):
            random_file = random.choice(files_of_author)
            files_of_author.remove(random_file)

            source = os.path.join(input_path, author_name, random_file)
            destination = os.path.join(test_path, author_name, random_file)
            shutil.copyfile(source, destination)

        for file_name in files_of_author:
            source = os.path.join(input_path, author_name, file_name)
            destination = os.path.join(training_path, author_name, file_name)
            shutil.copyfile(source, destination)
    # return num_documents_by_author
