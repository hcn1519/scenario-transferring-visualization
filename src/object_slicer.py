import yaml
import json
import copy
from typing import Optional, List, Tuple
from enum import Enum
from dataclasses import dataclass
from collections import defaultdict

class SamplingOption(Enum):
    PREFIX = 1
    SUFFIX = 2
    HALF = 3


class ObjectSlicer:
    @dataclass
    class Configuration:
        separator_keypaths: List[str]
        root_key_path: str = "" # if there are multiple top-level objects, we wrap it using root_key_path and treat it like a tree.
        max_number_of_elements: Tuple[int, SamplingOption] = (float('inf'), SamplingOption.PREFIX)

        def sorted_keypaths(self):
            return sorted(self.separator_keypaths, key=lambda x: len(x.split('.')), reverse=True)

    def __init__(self, configuration: Configuration):
        self.configuration = configuration
        self.all_keypaths = set()
        self.chunks = []

    def create_object_chunk_in_yaml_file(self, file_path: str):
        with open(file_path, "r") as file:
            yaml_data = file.read()
        return self.create_object_chunk_in_yaml_str(yaml_data)
        
    def create_object_chunk_in_yaml_str(self, input_str: str):
        dict_from_yaml = yaml.safe_load(input_str)
        return self.create_object_chunk(dict=dict_from_yaml)
    
    def create_object_chunk_in_json_file(self, file_path: str):
        with open(file_path, "r") as file:
            json_data = file.read()
        self.create_object_chunk_in_json_str(input_str=json_data)    

    def create_object_chunk_in_json_str(self, input_str: str):
        json_data_dict = json.loads(input_str)
        return self.create_object_chunk(dict=json_data_dict)

    def create_object_chunk(self, dict):
        if self.configuration.root_key_path and len(dict.keys()) > 1:
           dict = { self.configuration.root_key_path: dict }

        mutable_dict = copy.deepcopy(dict)
        
        if self.configuration.max_number_of_elements != float('inf'):
            mutable_dict = self.sample_elments(input_dict=mutable_dict)

        for separator_keypath in self.configuration.sorted_keypaths():
            self.update_chunks_by_keypath(data=mutable_dict, 
                                          keypath=separator_keypath, 
                                          original_keypath = separator_keypath)

        group_dict = defaultdict(list)
        for chunk in self.chunks:
            for key, value in chunk.items():
                new_key = key.split('.')[-1]
                group_dict[new_key].append(value)

        chunks = []
        for key, value in group_dict.items():
            chunks.append({key: value})

        self.chunks = chunks
        self.chunks.append(mutable_dict)
        return self.chunks

    def sample_elments(self, input_dict):

        def sampled_list(elements, sampling_option):
            (maximum_length, option) = sampling_option

            maximum_length = min(maximum_length, len(elements))

            if maximum_length == len(elements):
                return elements

            if option == SamplingOption.PREFIX:
                return elements[:maximum_length]
            elif option == SamplingOption.SUFFIX:
                return elements[-maximum_length:]

            right = maximum_length // 2
            left = maximum_length - right            
            return elements[:left] + elements[-right:] 
        
        res_dict = {}

        for key, value in input_dict.items():

            if isinstance(value, dict):
                new_value = self.sample_elments(input_dict=value)
                res_dict[key] = new_value
            elif isinstance(value, list):
                objects = sampled_list(elements = value, 
                                   sampling_option=self.configuration.max_number_of_elements)
                res_dict[key] = objects
            else:
                res_dict[key] = value
        return res_dict            

    def update_chunks_by_keypath(self, data, keypath, original_keypath):
        keys = keypath.split('.')

        if len(keys) > 1:
            new_key = keys[1:]
            
            if isinstance(data, list):
                for element in data:
                    self.update_chunks_by_keypath(data=element[keys[0]], 
                                                  keypath=".".join(new_key), 
                                                  original_keypath=original_keypath)
            else:
                self.update_chunks_by_keypath(data=data[keys[0]], 
                                              keypath=".".join(new_key), 
                                              original_keypath=original_keypath)
        elif len(keys) == 1:
            target_key = keys[0]
            if isinstance(data, list):
                chunk_list = []
                for i, element in enumerate(data):
                    chunk_list.append(copy.deepcopy(element[target_key]))
                    element[target_key] = f"<<Original Key Path: {original_keypath} {i}>>"
                self.chunks.append({original_keypath: chunk_list})
            else:
                chunk = {target_key: copy.deepcopy(data[target_key])}
                data[keys[0]] = f"<<Original Key Path: {original_keypath}>>"
                self.chunks.append(chunk)
    
    def retrieve_all_separator_keypaths(self, input, root_keypath: str):

        if isinstance(input, dict):
            self.all_keypaths.add(root_keypath)
            for key, value in input.items():

                if isinstance(value, dict):
                    self.retrieve_all_separator_keypaths(input = value, root_keypath=root_keypath +"."+ key)
                elif isinstance(value, list):
                    for obj in value:
                        self.retrieve_all_separator_keypaths(input=obj, root_keypath=root_keypath +"."+ key)
                else:
                    self.retrieve_all_separator_keypaths(input = value, root_keypath=root_keypath +"."+ key)
        else:
            new_key_path = root_keypath.split(".")[:-1]
            self.all_keypaths.add('.'.join(new_key_path))