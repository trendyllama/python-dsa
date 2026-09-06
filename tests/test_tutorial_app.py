from pathlib import Path

from fastapi.testclient import TestClient

from src.tutorial_app.api import build_app


def test_recipe_api_lists_seeded_recipes(tmp_path: Path) -> None:
    app = build_app(tmp_path / "recipes.db")

    with TestClient(app) as client:
        response = client.get("/api/recipes")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Fried egg"},
        {"id": 2, "name": "Butter toast"},
    ]


def test_recipe_api_returns_ordered_recipe_details(tmp_path: Path) -> None:
    app = build_app(tmp_path / "recipes.db")

    with TestClient(app) as client:
        response = client.get("/api/recipes/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Fried egg",
        "description": "Egg fried in butter",
        "ingredients": ["1 Egg", "1 pad of butter", "A pinch of salt"],
        "instructions": [
            "Melt butter in pan over medium-low heat",
            "Crack the egg into the buttered pan",
            "Sprinkle the pinch of salt onto the cooking egg",
            "Flip egg after about a minute and a half",
            "Serve egg after about a minute and a half",
        ],
    }


def test_recipe_api_returns_not_found_for_unknown_recipe(tmp_path: Path) -> None:
    app = build_app(tmp_path / "recipes.db")

    with TestClient(app) as client:
        response = client.get("/api/recipes/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Recipe not found"}
