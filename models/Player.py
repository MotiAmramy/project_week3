from dataclasses import dataclass

@dataclass
class Player:
    name : str
    position : str
    id : int = None
