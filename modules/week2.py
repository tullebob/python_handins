import argparse
def print_file_content(file):
    with open (file) as file_object:
        contents = file_object.read()
    print(contents)

#print_file_content('python_handin_template/modules/data_files/read_file.csv')

def write_list_to_file(output_file, lst):
    with open (output_file, 'w') as file_object:
        for tup in lst: 
            file_object.write(str(tup) + '\n')
    print('Der er skrevet til filen')

tupleList = [('test', 1), ('test', 2), ('test', 3)]

#write_list_to_file('my_notebooks/my_test/write_file.csv', tupleList)

def read_file(input_file):
    lines = []
    with open (input_file) as file_object:
        #lines = list(file)
        for line in file_object:
            line.strip()
            lines.append(line)
    print(lines)

#read_file('python_handin_template/modules/data_files/read_file.csv')

if __name__ == "__main__":
    """run with python w2.py input.txt -f output.txt -l word1 word2 word3"""
    parser = argparse.ArgumentParser(description='Solution to handin week 2')
    parser.add_argument('input_file', help='the input file to consume')
    parser.add_argument('-l', '--list', nargs='*', help='extra words', required=False) # nargs='*' means 0 or more args, nargs='+' means 1 or more
    parser.add_argument('-f', '--output_file', help='the file to print to. (console if nothing is given)')
    args = parser.parse_args()
    #print('INPUT:', args.input_file)
    #print('File:', args.output_file)
    #print('Len', vars(args))
    # only first arg
    if not (args.output_file and args.list):
        print_file_content(args.input_file)
    # only input and output
    else:
        lst = read_file(args.input_file)
        #if args.list:
         #   lst.extend(args.list)
        #print('LISTEN:',lst)
        write_list_to_file(args.output_file,args.list)   