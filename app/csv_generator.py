import csv
import multiprocessing
import os
import shutil
from typing import List

from app.types import FilePath
from app import ZipParser


class CSVGenerator:
    @staticmethod
    def generate_csv(zip_file_paths: List[FilePath], output_path: FilePath):
        if os.path.isdir(output_path):
            shutil.rmtree(output_path)

        os.mkdir(output_path)

        pool = multiprocessing.Pool()
        results = pool.map(ZipParser.parse_zip, zip_file_paths)

        contents_file_path = output_path + '/data.csv'
        objects_file_path = output_path + '/objects.csv'
        with open(contents_file_path, 'w', newline='') as csv_data_file, open(
            objects_file_path, 'w', newline=''
        ) as csv_objects_file:
            csv_data_writer = csv.writer(csv_data_file, delimiter='|')
            csv_objects_writer = csv.writer(csv_objects_file, delimiter='|')
            for result in results:
                for data in result:
                    csv_data_writer.writerow([data.uid, data.level])
                    for obj in data.objects:
                        csv_objects_writer.writerow([data.uid, obj.name])
