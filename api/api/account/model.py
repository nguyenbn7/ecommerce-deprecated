from pydantic import BaseModel


class SuccessResponse:
    def __init__(self, token: str, display_name: str, email: str) -> None:
        self.token = token
        self.display_name = display_name
        self.email = email

    token: str
    display_name: str
    email: str


class LoginDTO(BaseModel):
    email: str
    password: str


class RegisterDTO(BaseModel):
    email: str
    password: str


class AppUser:
    email: str = "bob@test.com"
    password_hash: str = "$2b$12$Fp7ady.Xio9zdHtBGWesauueVoG8rYqGy26ARRy5EjZFA5aQW0dP."
    display_name: str = "Bob"
