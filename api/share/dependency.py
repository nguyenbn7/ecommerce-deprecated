import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from share.setting import get_database_settings

_setting = get_database_settings()

_engine = create_engine(
    f"postgresql://{_setting.USER}:{_setting.PASSWORD}@{_setting.HOST}/{_setting.DB}",
    echo=True,
)
_Session = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


def get_db_session():
    db = _Session()
    try:
        yield db
    finally:
        db.close()


r = redis.Redis(decode_responses=True)


async def get_redis_session():
    try:
        yield r
    finally:
        r.close()
