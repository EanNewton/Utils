#!/usr/bin/python3

from os import path, getenv
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')
DEFAULT_DIR = path.dirname(path.abspath(__file__))