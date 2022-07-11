import os
import random
import shutil
import uuid
import zipfile
from typing import List
from xml.dom import minidom
from app.types import FilePath
from app.utils import generate_random_string


class Generator:
    def __init__(self):
        pass

    def generate_zip_files(
        self,
        number_of_zip: int,
        number_of_xml_in_zip: int,
        temp_dir_path: FilePath,
    ) -> List[FilePath]:
        if os.path.isdir(temp_dir_path):
            shutil.rmtree(temp_dir_path)

        os.mkdir(temp_dir_path)

        zip_file_paths = []
        for _ in range(number_of_zip):
            zip_file_name = generate_random_string() + ".zip"
            zip_file_path = temp_dir_path + zip_file_name
            zip_file = zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED)

            for _ in range(number_of_xml_in_zip):
                xml_file_name = generate_random_string() + ".xml"
                xml_string = self._generate_xml_string()
                xml_file_path = temp_dir_path + xml_file_name
                with open(xml_file_path, "w") as f:
                    f.write(xml_string)
                    f.close()
                zip_file.write(xml_file_path, xml_file_name)

            zip_file.close()
            zip_file_paths.append(zip_file_path)

        return zip_file_paths

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

