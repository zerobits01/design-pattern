import sys
import re

def main(file_path, output_path):
    # read file line by line
    file = open(file_path, "r")
    lines = file.readlines()
    file.close()

    text = ''
    for line in lines:
        if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
            text += line.rstrip('\n') + '\n'
        text = text.lstrip()
    with open(output_path, 'w+') as f:
        f.writelines([text])


main(sys.argv[1], sys.argv[2])