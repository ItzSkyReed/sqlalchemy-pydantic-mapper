from pydantic import ConfigDict, BaseModel
from sqlalchemy import Integer, String
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column

engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False, future=True)


class Base(DeclarativeBase):
    pass


class BadDB(Base):
    __tablename__ = "BAD"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)


class UserDB(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)


class StudentDB(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class StudSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class BadSchema(BaseModel):
    id: int
    name: str