
import os
import pytest
from src.plant_uml_image_generator import PlantUMLImageGenerator, Configuration, FileType
from src.object_slicer import ObjectSlicer, SamplingOption

@pytest.fixture(scope='session')
def project_root(pytestconfig):
    return pytestconfig.rootdir

def test_plant_uml_json_image_gen_half(project_root, tmp_path):

    file_path = os.path.join(project_root, "samples/story.json")
    
    separator_keypaths = [
        "Story.Act.ManeuverGroup"
    ]
    
    config = Configuration(file_type = FileType.JSON, 
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
    
    config = Configuration(file_type = FileType.JSON, 
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
    
    config = Configuration(file_type = FileType.JSON, 
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
