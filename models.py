from app import db
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer, DateTime, Text
from datetime import datetime
from typing import Optional
from dataclasses import dataclass


@dataclass
class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    birth_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    password: Mapped[str] = mapped_column(Text)

    def __init__(self, email, name, password, birth_date=None):
        self.email = email
        self.name = name
        self.password = password
        self.birth_date = birth_date
