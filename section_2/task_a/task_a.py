import sys


def get_filename():
    return sys.argv[1]


def main():
    with open(get_filename()) as file:
        for line in file.readlines():
            print line


if __name__ == '__main__':
    main()
