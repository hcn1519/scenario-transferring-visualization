
from dataclasses import dataclass
from typing import List
import json 

@dataclass
class LabeledDictionary:
    title: str
    chunk: dict

    def state_name(self) -> str:
        return "state_" + self.title.replace(".", "_")

class PlantUMLFormatter:

    def __init__(self, labeled_dictionaries: List[LabeledDictionary]) -> None:
        self.content = ""
        self.edges = []
        self.labeled_dictionaries = labeled_dictionaries
        
        for labeled_dict in self.labeled_dictionaries:
            json_string_chunk = json.dumps(labeled_dict.chunk, indent=2)
            key = list(labeled_dict.chunk.keys())[0]
            
            formatted_json = self.format_json_state_diagram(container_name = key, json_string = json_string_chunk)
            self.content += self.wrap_content_into_state(state_name = labeled_dict.title, content=formatted_json)
        

    def format_json_state_diagram(self, container_name: str, json_string: str) -> str:
        return f"json {container_name} {json_string}\n"
    
    def wrap_content_into_state(self, state_name: str, content: str) -> str:
        type_name = "state_" + state_name.replace(".", "_")
        
        return ''.join((
            f'state \"{state_name}\" as {type_name} {{\n',
            f'  {content}\n',
            f'}}\n'
        ))
    
    def add_edge(self, from_node: LabeledDictionary, to_node: LabeledDictionary):
        res = [f'{from_node.state_name()} --> {to_node.state_name()}\n']
        res.append(f'note on link\n')
        res.append(f'  {from_node.title} contains {to_node.title}\n')
        res.append("end note\n\n")
        self.edges.append(''.join(res))

    def add_edges(self, from_state: str, to_state: str):

        from_node = next(x for x in self.labeled_dictionaries if x.title == from_state)
        to_node = next(x for x in self.labeled_dictionaries if x.title == to_state)

        if not from_node or not to_node:
            return
        self.add_edge(from_node=from_node, to_node=to_node)
        
    def draw_composition_relationships(self):
        sorted_labeled_dicts = sorted(self.labeled_dictionaries, key=lambda x: x.title, reverse=True)

        for i, cur in enumerate(sorted_labeled_dicts):
            for next in sorted_labeled_dicts[i + 1:]:
                if next.title in cur.title:
                    self.add_edge(from_node=next, to_node=cur)
                    break
            
    def get_result(self) -> str:
        start = "@startuml\nleft to right direction\n\n"
        edges = ''.join(self.edges)
        end = "\n@enduml"
        return start + self.content + edges + end
        