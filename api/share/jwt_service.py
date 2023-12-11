from datetime import datetime, timedelta

from jose import jwt
from jose.constants import ALGORITHMS

from share.setting import get_token_service_settings

_setting = get_token_service_settings()


def create_jwt_token(claims: dict, token_live: timedelta, algorithm=ALGORITHMS.HS256):
    claims.update({"exp": datetime.utcnow() + token_live})
    encoded_jwt = jwt.encode(claims, _setting.SECRET_KEY, algorithm)
    return encoded_jwt


def generate_jwt_token(
    claims: dict, token_live_seconds: float, algorithm=ALGORITHMS.HS256
):
    return create_jwt_token(claims, timedelta(seconds=token_live_seconds), algorithm)


def decode_jwt_token(token: str | bytes, algorithm=ALGORITHMS.HS256):
    try:
        return jwt.decode(token, _setting.SECRET_KEY, algorithm)
    except Exception as e:
        raise e
