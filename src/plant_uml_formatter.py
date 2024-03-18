
from dataclasses import dataclass
from typing import List, Optional
import json
from enum import Enum

@dataclass
class LabeledDictionary:
    title: str
    chunk: dict

    def state_name(self) -> str:
        return "state_" + self.title.replace(".", "_")

@dataclass
class EdgeOption:
    class EdgeStyle(Enum):
        BOLD = "bold"
        DOTTED = "dotted"
        DASHED = "dashed"
    
    hex_color_str: str
    style: EdgeStyle = EdgeStyle.BOLD

    def edge_option_str(self) -> str:
        return f"[{self.style.value},#{self.hex_color_str}]"

class PlantUMLFormatter:

    def __init__(self, labeled_dictionaries: List[LabeledDictionary], wrapping_state_name: Optional[str] = None) -> None:
        self.content = ""
        self.edges = []
        self.labeled_dictionaries = labeled_dictionaries
        
        for labeled_dict in self.labeled_dictionaries:
            json_string_chunk = json.dumps(labeled_dict.chunk, indent=2)
            key = list(labeled_dict.chunk.keys())[0]
            
            formatted_json = self.format_json_state_diagram(container_name = key, json_string = json_string_chunk)
            self.content += self.wrap_content_into_state(state_name = labeled_dict.title, content=formatted_json)
        
        if wrapping_state_name:
            self.content = self.wrap_content_into_state(state_name = wrapping_state_name, 
                                                        content=self.content)

    def format_json_state_diagram(self, container_name: str, json_string: str) -> str:
        return f"json {container_name} {json_string}\n"
    
    def wrap_content_into_state(self, state_name: str, content: str) -> str:
        type_name = "state_" + state_name.replace(".", "_")
        
        return ''.join((
            f'state \"{state_name}\" as {type_name} {{\n',
            f'  {content}\n',
            f'}}\n'
        ))
    
    def add_composition_edge(self, from_node: LabeledDictionary, to_node: LabeledDictionary):
        option = EdgeOption(hex_color_str="000000")
        notes = [f'  {from_node.title} contains {to_node.title}\n']
        self.add_edge(from_node=from_node, to_node=to_node, edge_option=option, notes=notes)
    
    def add_edge(self, from_node_key: str, to_node_key: str, edge_option: EdgeOption, notes: List[str]):

        from_node = next((obj for obj in self.labeled_dictionaries if obj.title == from_node_key), None)
        to_node = next((obj for obj in self.labeled_dictionaries if obj.title == to_node_key), None)

        if not from_node or not to_node:
            print("error!")
            return
        self.add_edge(from_node=from_node, to_node=to_node, edge_option=edge_option, notes=notes)

    def add_edge(self, from_node: LabeledDictionary, to_node: LabeledDictionary, edge_option: EdgeOption, notes: List[str]):
        edge_str = PlantUMLFormatter.edge_str(from_node_str=from_node.title, 
                                              to_node_str=to_node.title, 
                                              edge_option=edge_option, 
                                              notes=notes)
        self.edges.append(edge_str)

    def draw_composition_relationships(self):
        sorted_labeled_dicts = sorted(self.labeled_dictionaries, key=lambda x: x.title, reverse=True)

        for i, cur in enumerate(sorted_labeled_dicts):
            for next in sorted_labeled_dicts[i + 1:]:
                if next.title in cur.title:
                    self.add_composition_edge(from_node=next, to_node=cur)
                    break

    def get_result(self) -> List[str]:
        start = "@startuml\nleft to right direction\n\n"
        edges = ''.join(self.edges)
        end = "\n@enduml"
        return [start, self.content, edges, end]
    
    @staticmethod
    def edge_str(from_node_str: str, to_node_str: str, edge_option: EdgeOption, notes: List[str]):
        def state_name(title: str) -> str:
            return "state_" + title.replace(".", "_")
    
        res = [f'{state_name(from_node_str)} -{edge_option.edge_option_str()}-> {state_name(to_node_str)}\n']
        if notes:
            res.append(f'note on link\n')
            for note in notes:
                res.append(note)
            res.append("end note\n\n")
        return ''.join(res)