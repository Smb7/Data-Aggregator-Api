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

    # 4. Assert the structure of each nested dictionary
    assert "total_playtime_hours" in data["steam_stats"]
    assert "games_owned" in data["steam_stats"]

    assert "gamerscore" in data["xbox_stats"]
    assert "recent_achievements" in data["xbox_stats"]

    assert "rank" in data["riot_stats"]
    assert "win_loss_ratio" in data["riot_stats"]