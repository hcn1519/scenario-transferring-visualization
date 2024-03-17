import os
import pytest
from src.plant_uml_image_generator import PlantUMLImageGenerator, Configuration, Format
from src.object_slicer import ObjectSlicer, SamplingOption

@pytest.fixture(scope='session')
def project_root(pytestconfig):
    return pytestconfig.rootdir

def test_plant_uml_generator_yaml(project_root):
    
    file_path = os.path.join(project_root, "samples/scenario_loc709.yml")
    with open(file_path, "r") as file:
        yaml_str = file.read()

    separator_keypaths = [
        "Scenario.OpenSCENARIO.Storyboard",
        "Scenario.OpenSCENARIO.Storyboard.Story",
        "Scenario.OpenSCENARIO.Entities",
    ]
    root_key_path="Scenario"

    config = Configuration(format_type = Format.YAML, 
                           object_slicer_configuration = ObjectSlicer.Configuration(root_key_path=root_key_path, 
                                                                                    separator_keypaths=separator_keypaths))
    generator = PlantUMLImageGenerator(config=config)
    gen_strs = generator.generate_uml_string_from_string(input_str=yaml_str)
    
    assert gen_strs[0].startswith("@startuml")
    assert gen_strs[0].endswith("@enduml")
    
def test_plant_uml_generator_non_separator(project_root):
    
    file_path = os.path.join(project_root, "samples/scenario_loc709.yml")
    with open(file_path, "r") as file:
        yaml_str = file.read()

    separator_keypaths = []
    root_key_path="Scenario"

    config = Configuration(format_type = Format.YAML, 
                           object_slicer_configuration = ObjectSlicer.Configuration(root_key_path=root_key_path, 
                                                                                    separator_keypaths=separator_keypaths))
    
    generator = PlantUMLImageGenerator(config=config)

    gen_strs = generator.generate_uml_string_from_string(input_str = yaml_str)
    
    assert gen_strs[0].startswith("@startuml")
    assert gen_strs[0].endswith("@enduml")


def test_plant_uml_yaml_image_gen(project_root, tmp_path):

    file_path = os.path.join(project_root, "samples/scenario_loc709.yml")
    
    separator_keypaths = [
        "Scenario.OpenSCENARIO.Storyboard",
        "Scenario.OpenSCENARIO.Storyboard.Story",
        "Scenario.OpenSCENARIO.Entities",
        "Scenario.OpenSCENARIO.Storyboard.Story.Act.ManeuverGroup",
    ]
    root_key_path="Scenario"
    
    config = Configuration(format_type = Format.YAML, 
                           object_slicer_configuration = ObjectSlicer.Configuration(root_key_path=root_key_path, 
                                                                                    separator_keypaths=separator_keypaths))
    generator = PlantUMLImageGenerator(config=config)
    
    uml_file_path = os.path.join(tmp_path, "sample.txt")
    output_file_path = os.path.join(tmp_path, "sample.png")

    # uml_file_path = os.path.join(project_root, "sample.txt")
    # output_file_path = os.path.join(project_root, "sample.png")

    with open(file_path, "r") as file:
        yaml_str = file.read()

    generator.generate_image_file(input_str=yaml_str, uml_file_path=uml_file_path)

    assert os.path.exists(uml_file_path)
    assert os.path.exists(output_file_path)

def test_plant_uml_json_image_gen(project_root, tmp_path):

    file_path = os.path.join(project_root, "samples/story.json")
    
    separator_keypaths = [
        "Story.Act"
    ]
    
    config = Configuration(format_type = Format.JSON, 
                           object_slicer_configuration = ObjectSlicer.Configuration(root_key_path="Story", 
                                                                                    separator_keypaths=separator_keypaths))
    
    generator = PlantUMLImageGenerator(config=config)
    
    with open(file_path, "r") as file:
        json_str = file.read()

    uml_file_path = os.path.join(tmp_path, "story.txt")
    output_file_path = os.path.join(tmp_path, "story.png")

    generator.generate_image_file(input_str=json_str, uml_file_path=uml_file_path)

    assert os.path.exists(uml_file_path)
    assert os.path.exists(output_file_path)


def test_plant_uml_yaml_image_gen_with_maximum_length(project_root, tmp_path):

    file_path = os.path.join(project_root, "samples/scenario_loc709.yml")
    
    separator_keypaths = [
        "Scenario.OpenSCENARIO.Storyboard",
        "Scenario.OpenSCENARIO.Storyboard.Story",
        "Scenario.OpenSCENARIO.Entities",
        "Scenario.OpenSCENARIO.Storyboard.Init.Actions.Private",
        "Scenario.OpenSCENARIO.Storyboard.Story.Act.ManeuverGroup",
    ]
    root_key_path="Scenario"
    
    config = Configuration(format_type = Format.YAML, 
                           object_slicer_configuration = ObjectSlicer.Configuration(root_key_path=root_key_path, 
                                                                                    separator_keypaths=separator_keypaths,
                                                                                    max_number_of_elements=(3, SamplingOption.HALF)))
    generator = PlantUMLImageGenerator(config=config)
    
    # uml_file_path = os.path.join(tmp_path, "sample.txt")
    # output_file_path = os.path.join(tmp_path, "sample.png")

    uml_file_path = os.path.join(project_root, "sample.txt")
    output_file_path = os.path.join(project_root, "sample.png")

    with open(file_path, "r") as file:
        yaml_str = file.read()

    generator.generate_image_file(input_str=yaml_str, uml_file_path=uml_file_path)

    assert os.path.exists(uml_file_path)
    assert os.path.exists(output_file_path)