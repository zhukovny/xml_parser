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
        results = pool.map(ZipParser.parse_zip, [zip_file_paths])

        contents_file_path = output_path + "contents.csv"
        objects_file_path = output_path + "objects.csv"
        with open(contents_file_path, "w", newline="") as csv_content_file, open(
            objects_file_path, "w", newline=""
        ) as csv_objects_file:
            csv_writer_1 = csv.writer(csv_content_file, delimiter=" ")
            csv_writer_2 = csv.writer(csv_objects_file, delimiter=" ")
            for result in results:
                for content in result:
                    csv_writer_1.writerow([content.uid, content.level])
                    for obj in content.objects:
                        csv_writer_2.writerow([content.uid, obj.name])
