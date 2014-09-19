
def odd_number_gen():
    num = 1
    while True:
        yield num
        num += 2

if __name__ == '__main__':

    num_gen = odd_number_gen()
    for i in range(100):
        print num_gen.next()
