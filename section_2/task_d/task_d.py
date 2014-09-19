import re


def word_count(word_list):

    res = {}

    for word in word_list:
        if word == '':
            continue
        if res.get(word):
            res[word] += 1
        else:
            res[word] = 1

    return res


def remove_stuff(word):
    return re.sub('[,.]', '', word)

if __name__ == '__main__':

    f = open('lorem.txt')
    contents = f.read()
    words = re.split(' |/n', contents)
    words = map(remove_stuff, words)

    print word_count(words)
