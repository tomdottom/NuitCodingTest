import sys
import re


def is_palindrome(word):

    word = re.sub('[".,!:? -]', '', word)
    word = re.sub("'", '', word)
    word = word.strip()
    word = word.lower()

    if len(word) == 0:
        return False

    if len(word) == 1:
        return True

    for index, char in enumerate(word):
        if word[index] != word[-index-1]:
            return False
        if index > len(word)-index:
            break

    return True


def get_filename(args):
    return args[1]


def get_file_contents_list(filename):
    contents = []
    with open(filename) as f:
        for line in f:
            contents.append(line)

    return contents


if __name__ == '__main__':

    filename = get_filename(sys.argv)
    contents = get_file_contents_list(filename)

    for word in contents:
        print '%s: %s' % (word.strip(), is_palindrome(word))
