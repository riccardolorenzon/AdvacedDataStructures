__author__ = 'riccardo'
# hash table to store the words based on a hash

def read_lines(input_file):
    with open(input_file, "r") as in_file:
        for line in in_file:
            print line
        in_file.close()

if __name__ == '__main__':
    read_lines('./story.txt')