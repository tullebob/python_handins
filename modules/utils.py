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