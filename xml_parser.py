import time

from app import CSVGenerator
from app import ZipGenerator

ZIP_FILES_NUM = 50
XML_FILES_NUM = 100
ZIP_FILES_PATH = './temp/'
CSV_FILES_PATH = './result/'


if __name__ == '__main__':
    print('Start zip generation...')
    zip_file_paths = ZipGenerator.generate_zip_files(ZIP_FILES_NUM, XML_FILES_NUM, ZIP_FILES_PATH)
    print('Zip files are generated.')

    print('Parse zip files and generate csv..')
    CSVGenerator.generate_csv(zip_file_paths, './result/')
    print('Done!')
