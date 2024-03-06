import configparser
import logging
import pathlib

import httpx

logging.basicConfig(level="INFO")
log = logging.getLogger(__name__)


SCRIPT_DIR = pathlib.Path(__file__).parent
API_VERSION = "v3"
BASE_URL = httpx.URL(f"https://www.googleapis.com/youtube/{API_VERSION}/")

log.info(f"{SCRIPT_DIR=}")
log.info(f"{API_VERSION=}")

CONFIG = configparser.ConfigParser()
CONFIG.read(SCRIPT_DIR / "configuration.ini")
API_KEY = CONFIG["core"]["API_KEY"]
CHANNELS = CONFIG["core"]["CHANNELS"]
