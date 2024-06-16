# config.py
# Author: Indrajit Ghosh
# Created On: Jun 12, 2024
# 
from pathlib import Path
from datetime import date

DOT_VAULTSAFE_DIR = Path.home() / '.vaultsafe' 

DATABASE_PATH = DOT_VAULTSAFE_DIR / 'vaultsafe.db'
DATABASE_URL = f'sqlite:///{DATABASE_PATH}'
DOT_SESSION_FILE = DOT_VAULTSAFE_DIR / '.session'

# Basic information
APP_NAME = "VaultSafe"
GITHUB_REPO = "https://github.com/indrajit912/VaultSafe.git"
CURRENT_YEAR = date.today().year
COPYRIGHT_STATEMENT = f"© {CURRENT_YEAR} Indrajit Ghosh. All rights reserved."
