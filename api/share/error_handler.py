class APIException(Exception):
    def __init__(
        self, status_code: int, message: str, headers: dict | None = None
    ) -> None:
        self.status_code = status_code
        self.message = message
        self.headers = headers
