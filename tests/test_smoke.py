import sys
from pathlib import Path

# Add <repo>/src to Python path so `import alien_invasion` works
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def test_can_import_package():
    import alien_invasion  # noqa: F401


def test_settings_has_basic_attrs():
    from alien_invasion.settings import Settings

    s = Settings()
    assert hasattr(s, "screen_width")
    assert hasattr(s, "screen_height")
