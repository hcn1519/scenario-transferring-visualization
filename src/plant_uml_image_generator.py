import os
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum
from src.object_slicer import ObjectSlicer
from src.plant_uml_formatter import PlantUMLFormatter, LabeledDictionary

class FileType(Enum):
    JSON = 'json'
    YAML = 'yaml'
    
@dataclass
class Configuration:
    file_type: FileType
    root_key_path: Optional[str]
    separators: List[str]


class PlantUMLImageGenerator:
    
    def __init__(self, config: Configuration):
        self.config = config
        self.slicer = ObjectSlicer(separator_keypaths=config.separators, root_key_path=config.root_key_path)
    
    def generate_string(self, input_str: str) -> str:
        chunks = []
        if self.config.file_type == FileType.YAML:
            chunks = self.slicer.create_object_chunk_in_yaml_str(input_str=input_str)
        else:
            chunks = self.slicer.create_object_chunk_in_json_str(input_str=input_str)

        if len(self.config.separators) == 0:
            title = self.config.root_key_path if self.config.root_key_path else list(chunks[0].keys())[0]
            uml_formatter = PlantUMLFormatter(labeled_dictionaries=[LabeledDictionary(title=title, chunk=chunks[0])])
            return uml_formatter.get_result()

        keypaths = self.slicer.separator_keypaths + [self.config.root_key_path]

        uml_formatter = PlantUMLFormatter(labeled_dictionaries=[LabeledDictionary(title=keypath, chunk=chunk) for chunk, keypath in zip(reversed(chunks), reversed(keypaths))])
        uml_formatter.draw_composition_relationships()
        return uml_formatter.get_result()
        
    def generate_image_file(self, input_str: str, uml_file_path: str, max_image_size: int=8192):        
        gen_str = self.generate_string(input_str=input_str)
        with open(uml_file_path, "w") as file:
            file.write(gen_str)

        jar_path = "./plantuml-mit-1.2024.3.jar"
        os.system(f'java -DPLANTUML_LIMIT_SIZE={max_image_size} -jar {jar_path} {uml_file_path}')
