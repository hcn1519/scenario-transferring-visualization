import os
import pytest
import yaml
from src.plant_uml_image_generator import PlantUMLImageGenerator, Configuration, Format
from src.object_slicer import ObjectSlicer, SamplingOption
from src.cyber_record_reader import CyberRecordReader, CyberRecordChannel
from src.relationship_director import RelationshipDirector, RelationshipDataSource as DataSource, RelationshipDataSourceConfiguration as Configuration
from protobuf_to_dict import protobuf_to_dict

@pytest.fixture(scope='session')
def project_root(pytestconfig):
    return pytestconfig.rootdir

def test_relationship(project_root):

    cyber_record_path = os.path.join(project_root, "samples/00000009.00000")
    openscenario_path = os.path.join(project_root, "samples/borregas_ego_routing.yaml")

    source_data = CyberRecordReader.read_channel(cyber_record_path, channel= CyberRecordChannel.ROUTING_REQUEST)

    routing_requests = CyberRecordReader.read_channel(source_path="./samples/00000009.00000", channel=CyberRecordChannel.ROUTING_REQUEST)
    routing_request = routing_requests[0]

    source_dict = protobuf_to_dict(routing_request)
    
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
        source=DataSource(configuration=Configuration(name="Apollo Scenario", object_slicer_configuration=source_config), 
                          source=source_dict),
        target=DataSource(configuration=Configuration(name="Autoware Scenario", object_slicer_configuration=target_config), 
                          source=target_dict)
        )
    
    uml_dest_path = os.path.join(project_root, "a.txt")
    director.create_image(uml_dest_path=uml_dest_path)

    assert director != None


    

