# Database
from sqlalchemy import create_engine

from core.setting import get_database_settings

s = get_database_settings()

engine = create_engine(
    f"postgresql://{s.USER}:{s.PASSWORD}@{s.HOST}/{s.DB}",
    echo=True,
)
