from typing import List
import yaml
import json
import copy
from typing import Optional

class ObjectSlicer:

    def __init__(self, separator_keypaths: List[str], root_key_path: Optional[str]):
        self.separator_keypaths = sorted(separator_keypaths, key=lambda x: len(x.split('.')), reverse=True)
        self.root_key_path = root_key_path # if there are multiple top-level objects, we wrap it using root_key_path and treat it like a tree.
        self.keypath_set = set()
        self.chunks = []

    def create_object_chunk_in_yaml(self, file_path: str):
        with open(file_path, "r") as file:
            yaml_data = file.read()

        dict_from_yaml = yaml.safe_load(yaml_data)
        return self.create_object_chunk(dict=dict_from_yaml)
    
    def create_object_chunk_in_json(self, file_path: str):
        with open(file_path, "r") as file:
            json_data_dict = json.load(file)
            
        return self.create_object_chunk(dict=json_data_dict)

    def create_object_chunk(self, dict):
        if self.root_key_path and len(dict.keys()) > 1:
           dict = { self.root_key_path: dict }

        mutable_dict = copy.deepcopy(dict)
        
        for separator_keypath in self.separator_keypaths:
            self.get_value_by_dot_path(data=mutable_dict, dot_path=separator_keypath, original_keypath = separator_keypath)

        self.chunks.append(mutable_dict)
        return self.chunks

    def get_value_by_dot_path(self, data, dot_path, original_keypath):
        keys = dot_path.split('.')

        if len(keys) > 1:
            new_key = keys[1:]
            if isinstance(data, list):
                for element in data:
                    self.get_value_by_dot_path(data=element[keys[0]], dot_path=".".join(new_key), original_keypath=original_keypath)
            else:
                self.get_value_by_dot_path(data=data[keys[0]], dot_path=".".join(new_key), original_keypath=original_keypath)
        elif len(keys) == 1:
            target_key = keys[0]
            if isinstance(data, list):
                chunk_list = []
                for i, element in enumerate(data):
                    chunk_list.append({target_key: copy.deepcopy(element[target_key])})
                    element[target_key] = f"<<Original Key Path: {original_keypath} {i}>>"
                self.chunks.append({target_key: chunk_list})
            else:
                chunk = {target_key: copy.deepcopy(data[target_key])}
                data[keys[0]] = f"<<Original Key Path: {original_keypath}>>"
                self.chunks.append(chunk)
        
    def retrieve_all_separator_keypaths(self, input, root_keypath: str):

        if isinstance(input, dict):
            self.keypath_set.add(root_keypath)
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
            self.keypath_set.add('.'.join(new_key_path))