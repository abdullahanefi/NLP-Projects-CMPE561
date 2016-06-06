from maxent import MaxentModel
import maxent
import sys


def baseline(sentences, labels):

    maxent.set_verbose(1)
    m = MaxentModel()
    m.begin_add_event()

    with open(sentences) as file_content:
        sentences = file_content.readlines()
    with open(labels) as file_content:
        labels = file_content.readlines()

    for i in xrange(0, 3000):
        m.add_event(sentences[i].split(" "), labels[i].strip())

    m.end_add_event()

    m.train()

    correct = 0
    false = 0

    for i in xrange(3000, len(sentences)):
        result = m.eval(sentences[i].split(" "), "1")
        result = int(round(result))
        label = int(labels[i])
        if result == label:
            correct = correct + 1
        else:
            false = false + 1

    print "correct   :", correct
    print "false     :", false

    print("accuracy  : {:.2f}%".format(correct * 100.0 / (correct + false)))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage : python2 baseline.py path_to_sentences path_to_labels"
        sys.exit(0)
    sentences = sys.argv[1]
    labels = sys.argv[2]
    baseline(sentences, labels)
