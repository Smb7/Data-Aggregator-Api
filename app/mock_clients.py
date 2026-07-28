import asyncio
from typing import Any, Dict


async def fetch_steam_data(gamer_tag: str) -> Dict[str, Any]:
    """
    Simulates fetching Steam data for a given gamer tag with a 0.5s delay.

    Args:
        gamer_tag: The gamer tag to fetch data for.

    Returns:
        A dictionary containing mock Steam stats.
    """
    await asyncio.sleep(0.5)
    return {"total_playtime_hours": 1500, "games_owned": 250}


async def fetch_xbox_data(gamer_tag: str) -> Dict[str, Any]:
    """
    Simulates fetching Xbox Live data for a given gamer tag with a 1.2s delay.
    """
    await asyncio.sleep(1.2)
    return {
        "gamerscore": 75000,
        "recent_achievements": ["Master Collector", "Legend of the Wastes"],
    }


async def fetch_riot_data(gamer_tag: str) -> Dict[str, Any]:
    """
    Simulates fetching Riot Games data for a given gamer tag with a 0.8s delay.
    """
    await asyncio.sleep(0.8)
    return {"rank": "Diamond IV", "win_loss_ratio": 1.2}