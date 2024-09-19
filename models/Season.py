from dataclasses import dataclass

@dataclass
class Season:
    player_id: None
    position: str
    age: int
    games: int
    games_started: int
    minutes_pg: float
    field_goals: int
    field_attempts: int
    field_percent: float
    three_fg: int
    three_attempts: int
    three_percent: float
    two_fg: int
    two_attempts: int
    two_percent: float
    effective_fg_percent: float
    ft: int
    ft_attempts: int
    ft_percent: float
    offensive_rb: int
    defensive_rb: int
    total_rb: int
    assists: int
    steals: int
    blocks: int
    turnovers: int
    personal_fouls: int
    points: int
    team: str
    season: int
    id: int = None

