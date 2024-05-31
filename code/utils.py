import os

def delete_all_files():
    DIR = 'files/'
    try:
        files = os.listdir(DIR)
        for file in files:
            FILE_PATH = os.path.join('files/',file)
            if os.path.isfile(FILE_PATH):
                os.remove(FILE_PATH)
        return '/n'
    except OSError:
        return 'error occurred while deleting files'

def create_directories():

    if not os.path.exists('files'):
        os.mkdir('files')

    if not os.path.exists('jj'):
        os.mkdir('jj')