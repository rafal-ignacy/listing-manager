from dataclasses import dataclass
from typing import Dict
import json


@dataclass
class JsonTemplate:
    def __init__(self, dictionary: Dict) -> None:
        self.dictionary: str = json.dumps(dictionary)

    def generate(self, variables: Dict) -> Dict:
        for key, value in variables.items():
            if isinstance(value, str) or isinstance(value, int) or isinstance(value, float):
                self.dictionary = self.dictionary.replace("{{ " + key + " }}", str(value))
            elif isinstance(value, list):
                list_string: str = ""
                for element in value:
                    list_string += "\"" + element + "\", "
                self.dictionary = self.dictionary.replace("[[\"{{ " + key + " }}\"]]", "[" + list_string[:-2] + "]")
            else:
                raise TypeError("Passed incorrect variable type!")
        return json.loads(self.dictionary)
