import logging

from fastapi import FastAPI, HTTPException, status, Path

from app.aggregator import get_aggregated_profile
from app.models import PlayerProfile


app = FastAPI(
    title="Data Aggregator API",
    description="A backend application that concurrently fetches data from public APIs and aggregates it.",
    version="0.1.0",
)

logger = logging.getLogger(__name__)


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to ensure the service is running.
    """
    return {"status": "healthy"}


@app.get(
    "/profile/{gamer_tag}",
    response_model=PlayerProfile,
    tags=["Player Profile"],
    summary="Get Aggregated Player Profile",
    description="Fetches and aggregates gaming stats for a given gamer tag from multiple sources concurrently.",
)
async def get_player_profile(
    gamer_tag: str = Path(
        ..., title="Gamer Tag", description="The username or gamer tag of the player to look up."
    )
) -> PlayerProfile:
    """
    Retrieves an aggregated player profile for the given gamer tag.

    This endpoint concurrently fetches player statistics from simulated Steam, Xbox Live,
    and Riot Games APIs. It then aggregates this data into a single, comprehensive
    player profile. If any of the individual platform API calls fail, the available
    data will still be returned, with the failed platform's stats marked as `null`.
    """
    try:
        profile = await get_aggregated_profile(gamer_tag)
        return profile
    except Exception as e:
        logger.error(f"An unexpected error occurred while fetching profile for {gamer_tag}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An internal error occurred while processing the request.",
        )

# Placeholder for future database setup
@app.on_event("startup")
async def startup_event():
    # This is where you would initialize the database connection
    print("Application startup...")

@app.on_event("shutdown")
async def shutdown_event():
    # This is where you would close the database connection
    print("Application shutdown...")