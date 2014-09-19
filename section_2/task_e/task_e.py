import json
import sys


def make_family_tree(induvidual_list):
    induvidual_list = json.loads(induvidual_list)

    family_map = {}

    for i in induvidual_list:
        family_map[i['id']] = i

    for i in family_map:
        if family_map[i].get('parent'):
            parent = family_map[i]['parent']
            if family_map[parent].get('sons'):
                family_map[parent]['sons'] += [i]
            else:
                family_map[parent]['sons'] = [i]

    family_list = [family_map[i] for i in family_map]

    return json.dumps(family_list)


def get_filename(args):
    return args[1]


def get_file_contents(filename):
    with open(filename) as f:
        contents = f.read()

    return contents


if __name__ == '__main__':

    filename = get_filename(sys.argv)
    contents = get_file_contents(filename)

    print make_family_tree(contents)
