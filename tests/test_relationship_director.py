import os
import pytest
import yaml
from src.plant_uml_image_generator import PlantUMLImageGenerator, Configuration, Format
from src.object_slicer import ObjectSlicer, SamplingOption
from src.cyber_record_reader import CyberRecordReader
from src.relationship_director import RelationshipDirector, RelationshipDataSource as DataSource, RelationshipDataSourceConfiguration as Configuration
from protobuf_to_dict import protobuf_to_dict
from collections import defaultdict

@pytest.fixture(scope='session')
def project_root(pytestconfig):
    return pytestconfig.rootdir

def test_relationship_routing_request(project_root):

    cyber_record_path = os.path.join(project_root, "samples/00000009.00000")
    openscenario_path = os.path.join(project_root, "samples/borregas_ego_routing.yaml")

    cyber_record_reader = CyberRecordReader()
    target_channel = CyberRecordReader.TargetChannels.ROUTING_REQUEST
    (routing_requests, _, _) = cyber_record_reader.read_channel(source_path=cyber_record_path,
                                                                channel=target_channel)

    assert len(routing_requests[target_channel.name]) == 1

    source_dict = routing_requests

    with open(openscenario_path, "r") as file:
        target_dict = yaml.safe_load(file)

    target_separator_keypaths = [
        "Scenario.OpenSCENARIO.Storyboard",
        "Scenario.OpenSCENARIO.Storyboard.Story",
        "Scenario.OpenSCENARIO.Entities",
    ]

    source_config = ObjectSlicer.Configuration(root_key_path="RoutingRequest", separator_keypaths=[])
    target_config = ObjectSlicer.Configuration(root_key_path="Scenario", 
                                               separator_keypaths=target_separator_keypaths,
                                               max_number_of_elements=(2, SamplingOption.HALF))

    director = RelationshipDirector(
        name="RoutingRequest",
        source=DataSource(configuration=Configuration(name="ApolloScenario", 
                                                      object_slicer_configuration=source_config), 
                          source=source_dict),
        target=DataSource(configuration=Configuration(name="AutowareScenario", 
                                                      object_slicer_configuration=target_config), 
                          source=target_dict)
        )
    
    uml_dest_path = os.path.join(project_root, "routing_request.txt")
    director.create_image(uml_dest_path=uml_dest_path)

    assert director != None

def test_relationship_obstacles(project_root):

    cyber_record_path = os.path.join(project_root, "samples/00000009.00000")
    openscenario_path = os.path.join(project_root, "samples/borregas_ego_routing.yaml")

    cyber_record_reader = CyberRecordReader()
    target_channel = CyberRecordReader.TargetChannels.PERCEPTION_OBSTACLES
    (obstacles, _, _) = cyber_record_reader.read_channel(source_path=cyber_record_path,
                                                         channel=target_channel)

    assert len(obstacles[target_channel.name]) == 677
    
    source_dict = obstacles
    
    with open(openscenario_path, "r") as file:
        target_dict = yaml.safe_load(file)

    source_separator_keypaths = [
        "PERCEPTION_OBSTACLES.perception_obstacle.polygon_point",
        "PERCEPTION_OBSTACLES.perception_obstacle.position",
        "PERCEPTION_OBSTACLES.perception_obstacle.velocity",
        "PERCEPTION_OBSTACLES.perception_obstacle.acceleration"
    ]

    target_separator_keypaths = [
        "Scenario.OpenSCENARIO.Storyboard",
        "Scenario.OpenSCENARIO.Storyboard.Story",
        "Scenario.OpenSCENARIO.Entities",
    ]

    source_config = ObjectSlicer.Configuration(root_key_path="PERCEPTION_OBSTACLES", 
                                               separator_keypaths=source_separator_keypaths,
                                               max_number_of_elements=(3, SamplingOption.PREFIX))
    target_config = ObjectSlicer.Configuration(root_key_path="Scenario", 
                                               separator_keypaths=target_separator_keypaths,
                                               max_number_of_elements=(2, SamplingOption.HALF))

    director = RelationshipDirector(
        name="Perception Obstacles",
        source=DataSource(configuration=Configuration(name="ApolloScenario", 
                                                      object_slicer_configuration=source_config), 
                          source=source_dict),
        target=DataSource(configuration=Configuration(name="AutowareScenario", 
                                                      object_slicer_configuration=target_config), 
                          source=target_dict)
        )
    
    uml_dest_path = os.path.join(project_root, "obstacle.txt")
    director.create_image(uml_dest_path=uml_dest_path)

    assert director != None