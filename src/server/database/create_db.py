from db_manager import base_manager
import sys

import settings

base_manager.create_base(settings.SCRIPTS_TABLES_PATH)