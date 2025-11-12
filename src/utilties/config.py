#Default configuration for phase 1 - using pydantic

from pathlib import Path
from typing import Literal
from pydantic import Field
from pydantic_setting import BaseSettings
import yaml

class SimulationConfig(BaseSettings):
    default_vvolume: float = 1.0
    default_cp: float = 4.18
    deafult_rho: float = 1000
    deafult_K0: float = 100
    default_ea: float = 50000
    default_dhr: float = 60000
    default_ua: float = 500