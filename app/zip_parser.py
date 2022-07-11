import zipfile
import xml.etree.ElementTree as ET
from typing import List
from uuid import UUID

from app.types import Data
from app.types import Object
from app.types import FilePath


class ZipParser:
    @staticmethod
    def parse_zip(zip_file_path: FilePath) -> List[Data]:
        contents = []
        zip_file = zipfile.ZipFile(zip_file_path, 'r')
        xml_file_names = zip_file.namelist()
        for xml_file_name in xml_file_names:
            xml_file_content = zip_file.read(xml_file_name)
            content = ZipParser._get_contents(xml_file_content)
            contents.append(content)

        return contents

    @staticmethod
    def _get_contents(xml_file_content: bytes) -> Data:
        root = ET.fromstring(xml_file_content)
        uid = UUID(root[0].attrib['value'])
        level = int(root[1].attrib['value'])
        objects_var = root[2]
        objects = [Object(name=obj.attrib['name']) for obj in objects_var]
        return Data(uid, level, objects)
