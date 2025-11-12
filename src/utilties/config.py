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

class PIDconfig(BaseSettings):
    default_kp: float = 5.0
    default_ki: float = 0.2
    default_kd: float = 1.0
    default_setpoint: float = 350.0
    default_dt: float = 1.0

class NeuralNetworkConfig(BaseSettings):
    default_architecture: Literal["lstm", "gru", "hybrid"] = "hybrid"
    default_hidden_units: int = 200
    default_lstm_layers: int = 2
    default_attention_heads: int = 4
    default_learning_rate: float = 1
    default_batch_size: int = 32
    default_epochs: int = 100
    sequence_window: int = 10

class Settings(BaseSettings):
    enviroment: str = "development"
    simulation: SimulationConfig = SimulationConfig()
    pid: PIDconfig = PIDconfig()
    neural_network: NeuralNetworkConfig = NeuralNetworkConfig()

class Config:
    env_file = ".env"

def load_config(config_path: str = "config.yaml") -> Settings:
    """Load configuration from YAML file"""
    with open(config_path, 'r') as f:
        config_dict = yaml.safe_load(f)
    return Settings(**config_dict)