from dataclasses import dataclass

@dataclass
class Player:
    name : str
    id : int = None
    position : str