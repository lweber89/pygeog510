"""Top-level package for pygeog510."""

__author__ = """Lloyd Weber"""
__email__ = "lweber89@gmail.com"
__version__ = "0.4.0"

# Explicitly import your modules or specific classes to avoid name collisions
from .foliumap import Map as foliumMap  # noqa: F401
from .pygeog510 import Map as ipyMap  # noqa: F401
