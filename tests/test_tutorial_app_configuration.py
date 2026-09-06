from src.tutorial_app.api.configuration import load_config, load_seed_recipes


def test_environment_config_overrides_base_and_keeps_base_values() -> None:
    config = load_config("prod")

    assert config.get("logging", "level") == "WARNING"
    assert config.get("logging", "file_name") == "/log/flask_template_tutorial.log"
    assert config.get("database", "uri") == "sqlite:///prod_database.db"
    assert config.get("app", "environment") == "PROD"


def test_seed_recipes_are_loaded_from_base_config() -> None:
    recipes = load_seed_recipes(load_config("pilot"))

    assert recipes[1]["name"] == "Fried egg"
    assert recipes[2]["description"] is None
    assert len(recipes[1]["instructions"]) == 5