__author__ = 'riccardo'
import hashlib
import operator

def upsert_hash_key(gram_type, s, hash_table):
    hash_key = hashlib.md5(s).hexdigest()
    if hash_key in hash_table:
        hash_table[hash_key][2] += 1
    else:
        hash_table[hash_key] = [gram_type, s, 1]

def read_lines(input_file, hash_table):
    """
    populate hash_table based on words contained in the input_file
    :param input_file: input file
    :param hash_table: hash table containing n-grams occurences
    :return:
    """
    with open(input_file, "r") as in_file:
        current_list, remainder = [], []
        while True:
            line1 = in_file.readline()
            if line1 == '':
                break
            current_list += line1.strip().split(' ')
            n = len(current_list)
            for i in xrange(0, n):
                s_2, s_3, s_4 = '','',''
                if n-i > 3:
                    #check if i + 1 exists
                    s_4 = ''.join(x for x in current_list[i:i+4])
                    upsert_hash_key(4, s_4, hash_table)
                    print '4gram ' + s_4
                if n-i > 2:
                    #check if i + 2 exists
                    s_3 = ''.join(x for x in current_list[i:i+3])
                    print '3gram ' + s_3
                    upsert_hash_key(3, s_3, hash_table)
                if n-i > 1:
                    #check if i + 3 exists
                    s_2 = ''.join(x for x in current_list[i:i+2])
                    print '2gram ' + s_2
                    upsert_hash_key(2, s_2, hash_table)
            current_list = current_list[-3:]
        in_file.close()

if __name__ == '__main__':
    hash_table = dict()
    read_lines('./story.txt', hash_table)

    four_grams = sorted([x[1] for x in hash_table.items() if x[1][0] == 4], key=operator.itemgetter(2), reverse = True)
    print 'first 10 4-grams : {0}'.format(four_grams)
    three_grams = sorted([x[1] for x in hash_table.items() if x[1][0] == 3], key=operator.itemgetter(2), reverse = True)
    print 'first 10 3-grams : {0}'.format(three_grams)
    two_grams = sorted([x[1] for x in hash_table.items() if x[1][0] == 2], key=operator.itemgetter(2), reverse = True)
    print 'first 10 2-grams : {0}'.format(two_grams)