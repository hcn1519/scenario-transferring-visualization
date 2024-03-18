import os
from dataclasses import dataclass
from typing import Optional, List, Tuple, Dict
from enum import Enum
from src.object_slicer import ObjectSlicer
from src.plant_uml_formatter import PlantUMLFormatter, LabeledDictionary, EdgeOption

class Format(Enum):
    JSON = 'json'
    YAML = 'yaml'
    DICT = 'dict'


@dataclass
class Relationship:
    src: str
    dest: str
    edge_option: EdgeOption
    

@dataclass
class Configuration:
    format_type: Format
    object_slicer_configuration: ObjectSlicer.Configuration
    relationships: List[Relationship]
    theme_map: Dict[str, str]
    wrapping_state_name: Optional[str] = None

    def root_key_path(self) -> str:
        return self.object_slicer_configuration.root_key_path

    def separator_keypaths(self) -> List[str]:
        return self.object_slicer_configuration.separator_keypaths
    
    def theme_str(self, keypath: str):
        if not keypath in self.theme_map:
            return ""
        return "#" + self.theme_map[keypath]

class PlantUMLImageGenerator:
    
    def __init__(self, config: Configuration):
        self.config = config
        self.slicer = ObjectSlicer(configuration=config.object_slicer_configuration)
    
    def generate_uml_string_from_dict(self, input_dict: Dict) -> List[str]:
        chunks = self.slicer.create_object_chunk(dict=input_dict)
        return self.generate_uml_string_from_chunks(chunks = chunks)
    
    def generate_uml_string_from_string(self, input_str: str) -> List[str]:
        chunks = []
        if self.config.format_type == Format.YAML:
            chunks = self.slicer.create_object_chunk_in_yaml_str(input_str=input_str)
        else:
            chunks = self.slicer.create_object_chunk_in_json_str(input_str=input_str)

        return self.generate_uml_string_from_chunks(chunks=chunks)
    
    def generate_uml_string_from_chunks(self, chunks) -> List[str]:
        
        if len(self.config.separator_keypaths()) == 0:    
            title = self.config.root_key_path() if self.config.root_key_path() else list(chunks[0].keys())[0]
            uml_formatter = PlantUMLFormatter(labeled_dictionaries=[LabeledDictionary(title=title, chunk=chunks[0], theme_str=self.config.theme_str(title))],
                                              wrapping_state_name = self.config.wrapping_state_name)
            return uml_formatter.get_result()

        keypaths = list(self.config.object_slicer_configuration.sorted_keypaths()) + [self.config.root_key_path()]

        uml_formatter = PlantUMLFormatter(labeled_dictionaries=[LabeledDictionary(title=keypath, chunk=chunk, theme_str=self.config.theme_str(keypath)) for chunk, keypath in zip(reversed(chunks), reversed(keypaths))],
                                          wrapping_state_name = self.config.wrapping_state_name)
        uml_formatter.draw_composition_relationships()

        for relationship in self.config.relationships:
            uml_formatter.add_edge(from_node_key=relationship.src, 
                                   to_node_key=relationship.dest, 
                                   edge_option=relationship.edge_option, 
                                   notes=relationship.notes)

        return uml_formatter.get_result()

    def generate_image_file(self, input_str: str, uml_file_path: str, max_image_size: int=16000) -> str:
        gen_strs = self.generate_uml_string_from_string(input_str=input_str)
        merged_str = ''.join(gen_strs)

        PlantUMLImageGenerator.generate_image_file_from_uml(uml_str= merged_str, 
                                                            uml_file_path=uml_file_path, 
                                                            max_image_size=max_image_size)

    @staticmethod
    def generate_image_file_from_uml(uml_str: str, uml_file_path: str, max_image_size: int=16000) -> str:
        with open(uml_file_path, "w") as file:
            file.write(uml_str)

        jar_path = "./plantuml-mit-1.2024.3.jar"
        print(f'java -DPLANTUML_LIMIT_SIZE={max_image_size} -jar {jar_path} {uml_file_path}')
        os.system(f'java -DPLANTUML_LIMIT_SIZE={max_image_size} -jar {jar_path} {uml_file_path}')
        return f"{uml_file_path}.png"

