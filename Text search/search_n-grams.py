__author__ = 'riccardo'
import hashlib

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
            token_type = 0
            for i in xrange(0, n-3):
                s_2, s_3, s_4 = '','',''
                if n-i > 2:
                    #check if i + 1 exists
                    s_4 = ''.join(x for x in current_list[i:i+4])
                    token_type = 4
                    print '4gram ' + s_2
                    hash_key = hashlib.md5(s_4).hexdigest()
                    if hash_key in hash_table:
                        hash_table[hash_key][2] += 1
                    else:
                        hash_table[hash_key] = [token_type, s_4, 0]
                if n-i > 1:
                    #check if i + 2 exists
                    s_3 = ''.join(x for x in current_list[i:i+3])
                    token_type = 3
                    print '3gram ' + s_2
                    hash_key = hashlib.md5(s_3).hexdigest()
                    if hash_key in hash_table:
                        hash_table[hash_key][2] += 1
                    else:
                        hash_table[hash_key] = [token_type, s_3, 0]
                if n-i > 0:
                    #check if i + 3 exists
                    s_2 = ''.join(x for x in current_list[i:i+2])
                    token_type = 2
                    print '2gram ' + s_2
                    hash_key = hashlib.md5(s_2).hexdigest()
                    if hash_key in hash_table:
                        hash_table[hash_key][2] += 1
                    else:
                        hash_table[hash_key] = [token_type, s_2, 0]
            current_list = current_list[-3:]
        in_file.close()

if __name__ == '__main__':
    hash_table = dict()
    read_lines('./story.txt', hash_table)
    print hash_table