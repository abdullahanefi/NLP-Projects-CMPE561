import re


def tokenize_file(filename):
    with open(filename, encoding="windows-1254") as file_content:
        lines = file_content.readlines()
    article = "\n".join(lines).strip().lower()

    return re.findall(r'[\wığüşöçĞÜŞİÖÇâÂî]+', article)
