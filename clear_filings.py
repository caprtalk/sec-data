import os
import glob


def clear_fillings(): # clears all sec filings from temp folder after they have been read
    path = os.path.dirname(__file__)
    src_folder = f'{path}/temp-sec-filings'
    # Search files with .xml extension in source directory
    file_type = r'/*.xml'
    files = glob.glob(src_folder + file_type)
    for file in files:
        os.remove(file)


clear_fillings()

