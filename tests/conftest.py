import os
import sys

# main.py opens a real display/audio device and loads assets at import time.
# Force pygame's headless (dummy) drivers before anything imports pygame.
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_DIR = os.path.dirname(_TESTS_DIR)  # .../Star-Ship-Shooter
_PROJECT_ROOT = os.path.dirname(_REPO_DIR)  # .../Space Shooter

# main.py loads assets via paths like "Star-Ship-Shooter/Assets/...", which
# are only valid relative to the project root, one level above the repo.
os.chdir(_PROJECT_ROOT)
sys.path.insert(0, _REPO_DIR)
