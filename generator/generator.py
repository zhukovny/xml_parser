import os
import random
import shutil
import uuid
import zipfile
from typing import List
from xml.dom import minidom

FilePath = str
TEMP_DIR = './tmp/'
XML_TEMP_DIR = TEMP_DIR + 'xml/'
NUM_OF_XML = 100
NUM_OF_ZIP = 50


def generate_random_string() -> str:
    return str(uuid.uuid4()).replace("-", "")


class Generator:
    def __init__(self):
        pass

    def generate_zip_files(self) -> List[FilePath]:
        if os.path.isdir(TEMP_DIR):
            shutil.rmtree(TEMP_DIR)

        os.mkdir(TEMP_DIR)
        os.mkdir(XML_TEMP_DIR)

        zip_file_paths = []
        print('Start zip generation...')
        for _ in range(NUM_OF_ZIP):
            xml_file_paths = []
            for _ in range(NUM_OF_XML):
                xml_file_name = generate_random_string()
                xml_string = self._generate_xml_string()
                xml_file_path = self._write_xml(xml_file_name, xml_string)
                xml_file_paths.append(xml_file_path)

            zip_file_name = generate_random_string()
            zip_file_path = self._write_zip(zip_file_name, xml_file_paths)
            zip_file_paths.append(zip_file_path)

        print('Done.')
        return zip_file_paths

    @staticmethod
    def _write_xml(file_name: str, xml_string: str) -> FilePath:
        file_path = XML_TEMP_DIR + file_name + ".xml"
        with open(file_path, "w") as f:
            f.write(xml_string)
            f.close()
        return file_path

    @staticmethod
    def _write_zip(file_name: str, xml_file_paths: List[FilePath]) -> FilePath:
        file_path = TEMP_DIR + file_name + ".zip"
        zip_file = zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED)
        for path in xml_file_paths:
            zip_file.write(path)
        zip_file.close()
        return file_path

    @staticmethod
    def _generate_xml_string() -> str:
        root = minidom.Document()
        xml = root.createElement('root')
        root.appendChild(xml)

        id_child = root.createElement('var')
        id_child.setAttribute('name', 'id')
        id_child.setAttribute('value', str(uuid.uuid4()))
        xml.appendChild(id_child)

        level_child = root.createElement('var')
        level_child.setAttribute('name', 'level')
        level_child.setAttribute('value', str(random.randint(1, 10)))
        xml.appendChild(level_child)

        objects_child = root.createElement('objects')
        for _ in range(random.randint(1, 10)):
            object_child = root.createElement('object')
            object_child.setAttribute('name', str(uuid.uuid4()).replace("-", ""))
            objects_child.appendChild(object_child)
        xml.appendChild(objects_child)

        return root.toprettyxml()

