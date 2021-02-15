import os
def get_file_names(folderpath, out= 'output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    fileNames = os.listdir(folderpath)
    print(fileNames)
    with open (out, 'w') as file_object:
        for f in fileNames:
            file_object.write(str(f) + '\n')
    print("Der er skrevet til filen.")
#get_file_names('my_notebooks/my_test', 'my_notebooks/my_test/write_file.csv')

#def get_all_file_names(folderpath,out=output.txt):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""

def print_line_one(*file_names):
    """takes a list of filenames and print the first line of each"""
    lines = []
    for file in file_names:
        with open(file) as file_object:
            lines.append("File: " + file +": " + file_object.readline()) 
    
    for line in lines:
        print(line.rstrip())


def print_emails(*file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    lines = []
    for file in file_names:
        with open(file) as file_object:
            line = file_object.readlines();
            for entry in line:
                if ('@' in entry):
                    lines.append("File: " + file +": " + entry)

    for line in lines:
        print(line.rstrip())

def write_headlines(*md_files, out='file_data/output3.txt'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    lines = []
    for file in md_files:
        with open(file) as file_object:
            line = file_object.readlines();
            for entry in line:
                if ('#' in entry):
                    lines.append("File: " + file +": " + entry)
        with open(out, 'w') as file_object:
            for field in lines:
                file_object.write(str(field))