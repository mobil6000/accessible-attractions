from pathlib import Path

from decouple import AutoConfig


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
PROJECT_PACKAGE_DIR = BASE_DIR / 'server'
config = AutoConfig(search_path=BASE_DIR)
