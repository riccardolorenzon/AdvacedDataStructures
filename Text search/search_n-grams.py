__author__ = 'riccardo'
import hashlib

def read_lines(input_file, hash_table):
    """
    populate hash_table based on words contained in the input_file
    :param input_file: input file
    :param hash_table: hash table containing n-grams occurences
    :return:
    """
    hash_object = hashlib.md5(b'Hello World')
    print(hash_object.hexdigest())
    with open(input_file, "r") as in_file:
        current_list, remainder = [], []
        while True:
            line1 = in_file.readline()
            if line1 == '':
                break
            current_list += line1.strip().split(' ')
            n = len(current_list)
            for i in xrange(0, n-3):
                s = ''
                print current_list[i]
                if n-3-i > 2:
                    #check if i + 1 exists
                    s = ''.join(x for x in current_list[i:4])
                    print s
                    pass
                elif n-3-i > 1:
                    #check if i + 2 exists
                    s = ''.join(x for x in current_list[i:3])
                    print s
                    pass
                elif n-3-i > 0:
                    #check if i + 3 exists
                    s = ''.join(x for x in current_list[i:2])
                    print s
                    pass
                else:
                    pass
            current_list = current_list[-3:]
        in_file.close()

if __name__ == '__main__':
    hash_table = dict()
    read_lines('./story.txt', hash_table)