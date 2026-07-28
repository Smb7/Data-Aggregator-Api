from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_profile_success():
    """
    Tests the successful retrieval of an aggregated player profile.
    """
    response = client.get("/profile/test_user")

    # 1. Assert the HTTP status code is 200 OK
    assert response.status_code == 200

    data = response.json()

    # 2. Assert the gamer_tag matches the request
    assert data["gamer_tag"] == "test_user"

    # 3. Assert the presence of the platform-specific stats blocks
    assert "steam_stats" in data
    assert "xbox_stats" in data
    assert "riot_stats" in data
 
    # 4. Assert the content and structure of each nested dictionary
    steam_stats = data["steam_stats"]
    assert steam_stats["total_playtime_hours"] == 1500
    assert steam_stats["games_owned"] == 250
 
    xbox_stats = data["xbox_stats"]
    assert xbox_stats["gamerscore"] == 75000
    assert xbox_stats["recent_achievements"] == ["Master Collector", "Legend of the Wastes"]
 
    riot_stats = data["riot_stats"]
    assert riot_stats["rank"] == "Diamond IV"
    assert riot_stats["win_loss_ratio"] == 1.2