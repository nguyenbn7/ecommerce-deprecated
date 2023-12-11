import re
from attr import dataclass
from pydantic import BaseModel, EmailStr, Field, model_validator
from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from share.model import BaseORM


class CustomerLogin(BaseModel):
    email: EmailStr = Field(examples=["tom@test.com"])
    password: str = Field(examples=["Pa$$w0rd"])


@dataclass(frozen=True)
class Authenticated:
    token: str
    email: str
    displayName: str


password_pattern = re.compile(
    r"(?=^.{6,10}$)(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&amp;*()_+}{&quot;:;'?/&gt;.&lt;,])(?!.*\s).*$"
)


class CustomerRegister(BaseModel):
    email: EmailStr = Field(examples=["tom@test.com"])
    displayName: str
    password: str = Field(examples=["Pa$$w0rd"])
    confirmPassword: str = Field(examples=["Pa$$w0rd"])

    @model_validator(mode="after")
    def check_passwords_match(self):
        pw1 = self.password
        if not password_pattern.match(pw1):
            raise ValueError(
                "Password must have 1 uppercase, 1 lowercase, 1 number, 1 non alphanumeric and at least 6 characters"
            )
        pw2 = self.confirmPassword
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError("password and confirm password do not match")
        return self


# Database Entity
class User(BaseORM):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_name: Mapped[str] = mapped_column(String(320), nullable=False)
    email: Mapped[str] = mapped_column(String(320), nullable=False)
    display_name: Mapped[str] = mapped_column(String(255), nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    normalized_email: Mapped[str] = mapped_column(String(320), nullable=False)
    normalized_user_name: Mapped[str] = mapped_column(String(320), nullable=False)

    address: Mapped["UserAddress"] = relationship(
        "UserAddress",
        back_populates="user",
        uselist=False,
    )


class UserAddress(BaseORM):
    __tablename__ = "user_addresses"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(256), nullable=False)
    street: Mapped[str] = mapped_column(String(400), nullable=False)
    city: Mapped[str] = mapped_column(String(256), nullable=False)
    state: Mapped[str] = mapped_column(String(256), nullable=False)
    zip_code: Mapped[str] = mapped_column(String(10), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="address")
