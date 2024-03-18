
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type, Dict, List, Tuple
from src.object_slicer import ObjectSlicer, SamplingOption
from src.plant_uml_formatter import PlantUMLFormatter, EdgeOption
from src.plant_uml_image_generator import PlantUMLImageGenerator, Configuration as PlantUMLImageGeneratorConfiguration, Format as PlantUMLImageGeneratorFormat, Relationship

class RelationshipDataSourceConfiguration:
    name: str
    relationships: List[Relationship]
    object_slicer_configuration: ObjectSlicer.Configuration

    def __init__(self, name: str, relationships: List[Relationship], object_slicer_configuration: ObjectSlicer.Configuration) -> None:
        self.name = name
        self.relationships = relationships
        self.object_slicer_configuration = object_slicer_configuration
        self.theme_map = {}
        
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
    relationships: List[Relationship]
    theme_map: Dict[str, str]
    source: RelationshipDataSource
    target: RelationshipDataSource

    def __init__(self, name: str, source: RelationshipDataSource, target: RelationshipDataSource, relationships: List[Relationship]) -> None:
        self.name = name
        self.source = source
        self.target = target
        self.theme_map = {}
        for relationship in relationships:
            self.theme_map[relationship.src] = relationship.edge_option.hex_color_str
            self.theme_map[relationship.dest] = relationship.edge_option.hex_color_str

        src_target_relationship = Relationship(src=self.source.configuration.name, 
                                               dest=self.target.configuration.name, 
                                               edge_option=EdgeOption(hex_color_str="FF0000"))
        self.relationships = [src_target_relationship] + relationships


    def create_image(self, uml_dest_path: str):

        source_config = PlantUMLImageGeneratorConfiguration(format_type = PlantUMLImageGeneratorFormat.DICT,
                                                            object_slicer_configuration = self.source.configuration.object_slicer_configuration,
                                                            wrapping_state_name=self.source.configuration.name,
                                                            relationships=self.source.configuration.relationships,
                                                            theme_map=self.theme_map)
        target_config = PlantUMLImageGeneratorConfiguration(format_type = PlantUMLImageGeneratorFormat.DICT,
                                                            object_slicer_configuration = self.target.configuration.object_slicer_configuration,
                                                            wrapping_state_name=self.target.configuration.name,
                                                            relationships=self.target.configuration.relationships,
                                                            theme_map=self.theme_map)
        
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

        relationship_edge_str = ""
        for relationship in self.relationships:
            edge = PlantUMLFormatter.edge_str(from_node_str=relationship.src, 
                                              to_node_str=relationship.dest,
                                              edge_option=relationship.edge_option,
                                              notes=[])
            relationship_edge_str += edge
        
        print("relationship_edge_str:", relationship_edge_str)
        result = start + source_content + target_content + source_edge + target_edge + relationship_edge_str + end

        PlantUMLImageGenerator.generate_image_file_from_uml(uml_str=result, uml_file_path=uml_dest_path)
        
