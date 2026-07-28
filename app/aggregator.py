import asyncio
import logging
from typing import Union

from app.mock_clients import fetch_riot_data, fetch_steam_data, fetch_xbox_data
from app.models import PlayerProfile, RiotStats, SteamStats, XboxStats

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def get_aggregated_profile(gamer_tag: str) -> PlayerProfile:
    """
    Concurrently fetches data from all gaming APIs and aggregates them into a single profile.

    Args:
        gamer_tag: The gamer tag to fetch data for.

    Returns:
        A PlayerProfile object containing the aggregated data.
    """
    tasks = [
        fetch_steam_data(gamer_tag),
        fetch_xbox_data(gamer_tag),
        fetch_riot_data(gamer_tag),
    ]

    results = await asyncio.gather(*tasks, return_exceptions=True)

    steam_result, xbox_result, riot_result = results

    steam_stats: Union[SteamStats, None] = None
    if not isinstance(steam_result, Exception):
        steam_stats = SteamStats(**steam_result)
    else:
        logger.warning(f"Failed to fetch Steam data for {gamer_tag}: {steam_result}")

    xbox_stats: Union[XboxStats, None] = None
    if not isinstance(xbox_result, Exception):
        xbox_stats = XboxStats(**xbox_result)
    else:
        logger.warning(f"Failed to fetch Xbox data for {gamer_tag}: {xbox_result}")

    riot_stats: Union[RiotStats, None] = None
    if not isinstance(riot_result, Exception):
        riot_stats = RiotStats(**riot_result)
    else:
        logger.warning(f"Failed to fetch Riot data for {gamer_tag}: {riot_result}")

    return PlayerProfile(
        gamer_tag=gamer_tag,
        steam_stats=steam_stats,
        xbox_stats=xbox_stats,
        riot_stats=riot_stats,
    )