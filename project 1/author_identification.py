#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author:  Abdullah Hanefi Önaldı
# Created: 25 Feb 2016

import os
import numpy as np

from collections import Counter
from math import log

from utils import list_dirs, list_files
from tokenizer import tokenize_file
from preprocessing import pre_process


def create_BOW(root_directory='./preprocessed_texts/'):
    """
    :type root_directory: str
    """
    training_path = os.path.join(root_directory, "training")

    training_bag_of_author = {}
    # super_counter = Counter()
    doc_count_of_author = {}

    authors = list_dirs(training_path)
    # total_doc_count = 0

    for author in authors:
        bag = Counter()

        author_path = os.path.join(training_path, author)
        files_of_author = list_files(author_path)

        for filename in files_of_author:
            file_path = os.path.join(author_path, filename)
            tokens = tokenize_file(file_path)
            bag += Counter(tokens)

        training_bag_of_author[author] = bag
        doc_count = len(files_of_author)
        doc_count_of_author[author] = doc_count
        # total_doc_count += doc_count

        # super_counter += bag

    # print(super_counter.most_common(10))
    return training_bag_of_author, doc_count_of_author


def calculate_probability_of_author(tokens, training_bags, doc_counts):
    """

    :type tokens: list
    :type training_bags: dict
    :type doc_counts: dict
    """
    authors = training_bags.keys()

    total_doc_count = sum(doc_counts.values())
    probabilities = {author:
                     log(doc_counts[author]) - log(total_doc_count)
                     for author in authors}
    vocabulary_sizes = dict((author, sum(training_bags[author].values()))
                            for author in authors)

    alpha = 0.005
    alpha_denominator = alpha * len(authors)

    for token in tokens:
        # common_denominator = 0
        for author in authors:
            count = training_bags[author][token]
            # common_denominator += count
            # print("vocab size : ", vocabulary_sizes[author], " count ",count)
            # print("   and log is : ", log(count/vocabulary_sizes[author]))
            probabilities[author] += log(count + alpha) - \
                log(vocabulary_sizes[author] + alpha_denominator)

    # print(probabilities)
    return Counter(probabilities).most_common(1)


def calculate_confusion_matrix(training_bags, doc_counts,
                               output_path='./preprocessed_texts/'):
    authors = list(training_bags.keys())
    confusion_matrix = np.zeros([len(authors), len(authors)], dtype=np.integer)

    test_path = os.path.join(output_path, "test")

    for i, author in enumerate(authors):
        # bag = Counter()
        author_path = os.path.join(test_path, author)
        files_of_author = list_files(author_path)

        for filename in files_of_author:
            file_path = os.path.join(author_path, filename)
            tokens = tokenize_file(file_path)
            author_candidates = calculate_probability_of_author(
                tokens=tokens,
                training_bags=training_bags,
                doc_counts=doc_counts)
            candidate_index = authors.index(author_candidates[0][0])
            confusion_matrix[i, candidate_index] += 1
    # print(confusion)
    return confusion_matrix


if __name__ == "__main__":
    print("main func")
    num_documents_by_author = pre_process()
    training_bag_of_author, doc_count_of_author = create_BOW()
    confusion = calculate_confusion_matrix(
        training_bags=training_bag_of_author, doc_counts=doc_count_of_author)
    # print(confusion)
    np.savetxt('confusion.txt', confusion, fmt='%d')
    print('tp : {:.2f}%'.
          format(100 * sum(np.diag(confusion)) / sum(sum(confusion))))
