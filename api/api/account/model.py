from dataclasses import dataclass
from pydantic import BaseModel, EmailStr, field_validator, model_validator
from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from share.model import BaseORM


@dataclass(frozen=True)
class SuccessResponse:
    token: str
    email: str
    display_name: str


class LoginDTO(BaseModel):
    email: EmailStr
    password: str


class RegisterDTO(BaseModel):
    email: EmailStr
    display_name: str
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def check_passwords_match(self):
        pw1 = self.password
        pw2 = self.confirm_password
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError("password and confirm password do not match")
        return self


class ApplicationUser(BaseORM):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_name: Mapped[str] = mapped_column(String(320), nullable=False)
    email: Mapped[str] = mapped_column(String(320), nullable=False)
    display_name: Mapped[str] = mapped_column(String(255), nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    normalized_email: Mapped[str] = mapped_column(String(320), nullable=False)
    normalized_user_name: Mapped[str] = mapped_column(String(320), nullable=False)

    address: Mapped["ApplicationUserAddress"] = relationship(
        "ApplicationUserAddress",
        back_populates="user",
        uselist=False,
    )


class ApplicationUserAddress(BaseORM):
    __tablename__ = "user_addresses"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(256), nullable=False)
    last_name: Mapped[str] = mapped_column(String(256), nullable=False)
    street: Mapped[str] = mapped_column(String(400), nullable=False)
    city: Mapped[str] = mapped_column(String(256), nullable=False)
    state: Mapped[str] = mapped_column(String(256), nullable=False)
    zip_code: Mapped[str] = mapped_column(String(10), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["ApplicationUser"] = relationship(
        "ApplicationUser", back_populates="address"
    )
