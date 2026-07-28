from typing import List, Optional

from pydantic import BaseModel


class SteamStats(BaseModel):
    """Pydantic model for Steam statistics."""

    total_playtime_hours: int
    games_owned: int


class XboxStats(BaseModel):
    """Pydantic model for Xbox statistics."""

    gamerscore: int
    recent_achievements: List[str]


class RiotStats(BaseModel):
    """Pydantic model for Riot Games statistics."""

    rank: str
    win_loss_ratio: float


class PlayerProfile(BaseModel):
    """Unified Pydantic model for a player's aggregated profile."""

    gamer_tag: str
    steam_stats: Optional[SteamStats] = None
    xbox_stats: Optional[XboxStats] = None
    riot_stats: Optional[RiotStats] = None