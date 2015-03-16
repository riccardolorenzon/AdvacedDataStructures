import operator

def upsert_hash_key(gram_type, s, hash_table):
    hash_key = s
    if hash_key in hash_table:
        hash_table[hash_key][1] += 1
    else:
        hash_table[hash_key] = [gram_type, 1]

def read_lines(lines, hash_table):
    """
    populate hash_table based on words contained in the input_file
    :param input_file: input file
    :param hash_table: hash table containing n-grams occurences
    :return:
    """
    current_list, remainder = [], []
    for line_number, line1 in enumerate(lines):
        current_list += line1.strip().split(' ')
        n = len(current_list)
        for i in xrange(0, n):
            if n-i < 4 and line_number != len(lines) - 1:
                continue
            s_2, s_3, s_4 = '','',''
            if n-i > 3:
                #check if i + 1 exists
                s_4 = ' '.join(x for x in current_list[i:i+4])
                upsert_hash_key(4, s_4, hash_table)
            if n-i > 2:
                #check if i + 2 exists
                s_3 = ' '.join(x for x in current_list[i:i+3])
                upsert_hash_key(3, s_3, hash_table)
            if n-i > 1:
                #check if i + 3 exists
                s_2 = ' '.join(x for x in current_list[i:i+2])
                upsert_hash_key(2, s_2, hash_table)
        current_list = current_list[-3:]

if __name__ == '__main__':
    hash_table = dict()
    file_input = raw_input('please input the full path name : ')
    with open(file_input, "r") as in_file:
        lines = in_file.readlines()
        read_lines(lines, hash_table)
    four_grams = sorted([x for x in hash_table.iteritems() if x[1][0] == 4], \
                        key=operator.itemgetter(1,1), reverse = True)
    print 'first 10 4-grams : {0}'.format(four_grams)
    three_grams = sorted([x for x in hash_table.iteritems() if x[1][0] == 3], \
                         key=operator.itemgetter(1), reverse = True)
    print 'first 10 3-grams : {0}'.format(three_grams)
    two_grams = sorted([x for x in hash_table.iteritems() if x[1][0] == 2], \
                       key=lambda(k,v) : v[1], reverse = True)
    print 'first 10 2-grams : {0}'.format(two_grams)
