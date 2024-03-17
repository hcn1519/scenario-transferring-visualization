
from abc import ABC, abstractmethod
from typing import Type, Dict, List, Tuple
from src.object_slicer import ObjectSlicer, SamplingOption
from src.plant_uml_formatter import PlantUMLFormatter
from src.plant_uml_image_generator import PlantUMLImageGenerator, Configuration as PlantUMLImageGeneratorConfiguration, Format as PlantUMLImageGeneratorFormat

class RelationshipDataSourceConfiguration:
    name: str
    object_slicer_configuration: ObjectSlicer.Configuration

    def __init__(self, name: str, object_slicer_configuration: ObjectSlicer.Configuration) -> None:
        self.name = name
        self.object_slicer_configuration = object_slicer_configuration
        
    # shortcut methods

    def root_key_path(self) -> str:
        return self.object_slicer_configuration.root_key_path

    def separator_keypaths(self) -> List[str]:
        return self.object_slicer_configuration.separator_keypaths

    def max_number_of_elements(self) -> Tuple[int, SamplingOption]:
        return self.object_slicer_configuration.max_number_of_elements


class RelationshipDataSource:
    configuration: RelationshipDataSourceConfiguration
    source: Dict

    def __init__(self, configuration: RelationshipDataSourceConfiguration, source: Dict) -> None:
        self.configuration = configuration
        self.source = source


class RelationshipDirector:
    name: str
    source: RelationshipDataSource
    target: RelationshipDataSource

    def __init__(self, name: str, source: RelationshipDataSource, target: RelationshipDataSource) -> None:
        self.name = name
        self.source = source
        self.target = target

    def merged_config(self) -> PlantUMLImageGeneratorConfiguration:

        source_config = PlantUMLImageGeneratorConfiguration(format_type = PlantUMLImageGeneratorFormat.DICT,
                                                            object_slicer_configuration = self.source.configuration.object_slicer_configuration)
        return PlantUMLImageGeneratorConfiguration(format_type = PlantUMLImageGeneratorFormat.DICT,
                                                   object_slicer_configuration = self.target.configuration.object_slicer_configuration)
        

    def create_image(self, uml_dest_path: str):


        source_config = PlantUMLImageGeneratorConfiguration(format_type = PlantUMLImageGeneratorFormat.DICT,
                                                            object_slicer_configuration = self.source.configuration.object_slicer_configuration)
        target_config = PlantUMLImageGeneratorConfiguration(format_type = PlantUMLImageGeneratorFormat.DICT,
                                                            object_slicer_configuration = self.target.configuration.object_slicer_configuration)
        
        source_generator = PlantUMLImageGenerator(config=source_config)
        source_strs = source_generator.generate_uml_string_from_dict(input_dict=self.source.source)

        target_generator = PlantUMLImageGenerator(config=target_config)
        target_strs = target_generator.generate_uml_string_from_dict(input_dict=self.target.source)

        start = source_strs[0]
        end = source_strs[-1]

        source_content = source_strs[1]
        target_content = target_strs[1]
        source_edge = source_strs[2]
        target_edge = target_strs[2]

        result = start + source_content + target_content + source_edge + target_edge + end

        merged_generator = PlantUMLImageGenerator(config=self.merged_config())
        merged_generator.generate_image_file_from_uml(uml_str=result, uml_file_path=uml_dest_path)

