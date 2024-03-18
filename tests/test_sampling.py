
import os
import yaml
import pytest
from src.plant_uml_image_generator import PlantUMLImageGenerator, Configuration, Format
from src.object_slicer import ObjectSlicer, SamplingOption

@pytest.fixture(scope='session')
def project_root(pytestconfig):
    return pytestconfig.rootdir

def test_plant_uml_json_image_gen_half(project_root, tmp_path):

    file_path = os.path.join(project_root, "samples/story.json")
    
    separator_keypaths = [
        "Story.Act.ManeuverGroup"
    ]
    
    config = Configuration(format_type = Format.JSON, 
                           object_slicer_configuration = ObjectSlicer.Configuration(root_key_path="Story", 
                                                                                    separator_keypaths=separator_keypaths,
                                                                                    max_number_of_elements=(3, SamplingOption.HALF)))
    
    generator = PlantUMLImageGenerator(config=config)
    
    with open(file_path, "r") as file:
        json_str = file.read()

    uml_file_path = os.path.join(tmp_path, "story-half.txt")
    output_file_path = os.path.join(tmp_path, "story-half.png")

    generator.generate_image_file(input_str=json_str, uml_file_path=uml_file_path)

    assert os.path.exists(uml_file_path)
    assert os.path.exists(output_file_path)

def test_plant_uml_json_image_gen_prefix(project_root, tmp_path):

    file_path = os.path.join(project_root, "samples/story.json")
    
    separator_keypaths = [
        "Story.Act.ManeuverGroup"
    ]
    
    config = Configuration(format_type = Format.JSON, 
                           object_slicer_configuration = ObjectSlicer.Configuration(root_key_path="Story", 
                                                                                    separator_keypaths=separator_keypaths,
                                                                                    max_number_of_elements=(5, SamplingOption.PREFIX)))
    
    generator = PlantUMLImageGenerator(config=config)
    
    with open(file_path, "r") as file:
        json_str = file.read()

    uml_file_path = os.path.join(tmp_path, "story-prefix.txt")
    output_file_path = os.path.join(tmp_path, "story-prefix.png")

    generator.generate_image_file(input_str=json_str, uml_file_path=uml_file_path)

    assert os.path.exists(uml_file_path)
    assert os.path.exists(output_file_path)


def test_plant_uml_json_image_gen_suffix(project_root, tmp_path):

    file_path = os.path.join(project_root, "samples/story.json")
    
    separator_keypaths = [
        "Story.Act.ManeuverGroup"
    ]
    
    config = Configuration(format_type = Format.JSON, 
                           object_slicer_configuration = ObjectSlicer.Configuration(root_key_path="Story", 
                                                                                    separator_keypaths=separator_keypaths,
                                                                                    max_number_of_elements=(6, SamplingOption.SUFFIX)))
    
    generator = PlantUMLImageGenerator(config=config)
    
    with open(file_path, "r") as file:
        json_str = file.read()

    uml_file_path = os.path.join(tmp_path, "story-suffix.txt")
    output_file_path = os.path.join(tmp_path, "story-suffix.png")

    generator.generate_image_file(input_str=json_str, uml_file_path=uml_file_path)

    assert os.path.exists(uml_file_path)
    assert os.path.exists(output_file_path)

def test_get_all_key_paths(project_root):

    file_path = os.path.join(project_root, "samples/scenario_loc709.yml")
    with open(file_path, "r") as file:
        yaml_obj = yaml.safe_load(file)

    object_slicer_configuration = ObjectSlicer.Configuration(root_key_path="Secenario", 
                                                             separator_keypaths=[],
                                                             max_number_of_elements=(2, SamplingOption.PREFIX))

    object_slicer = ObjectSlicer(configuration=object_slicer_configuration)
    object_slicer.retrieve_all_separator_keypaths(input = yaml_obj, 
                                                  root_keypath=object_slicer_configuration.root_key_path)

    assert "Secenario.OpenSCENARIO.Entities" in object_slicer.all_keypaths
    assert "Secenario.OpenSCENARIO" in object_slicer.all_keypaths
    assert "Secenario.OpenSCENARIO.RoadNetwork.TrafficSignals" in object_slicer.all_keypaths

def test_slicing(project_root):

    file_path = os.path.join(project_root, "samples/scenario_loc709.yml")
    with open(file_path, "r") as file:
        yaml_obj = yaml.safe_load(file)

    object_slicer_configuration = ObjectSlicer.Configuration(root_key_path="Secenario", 
                                                             separator_keypaths=[],
                                                             max_number_of_elements=(3, SamplingOption.PREFIX))

    object_slicer = ObjectSlicer(configuration=object_slicer_configuration)
    chunks = object_slicer.create_object_chunk(dict = yaml_obj)

    assert len(chunks) == 1
    assert len(chunks[0]["Secenario"]["OpenSCENARIO"]["ParameterDeclarations"]["ParameterDeclaration"]) == 3
