# Database
from sqlalchemy import create_engine

from core.setting import get_database_settings

_setting = get_database_settings()

engine = create_engine(
    f"postgresql://{_setting.USER}:{_setting.PASSWORD}@{_setting.HOST}/{_setting.DB}",
    echo=True,
)
