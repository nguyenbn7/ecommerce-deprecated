from functools import lru_cache
from core.setting import CorsSetting, DatabaseSetting, TokenServiceSetting


@lru_cache
def get_database_settings():
    return DatabaseSetting()


@lru_cache
def get_cors_settings():
    return CorsSetting()


@lru_cache
def get_token_service_settings():
    return TokenServiceSetting()
