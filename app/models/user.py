from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.db.database import Base
from sqlalchemy import String
from app.models.task import Task

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )

    hashed_password: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    tasks: Mapped[list[Task]] = relationship(
        "Task",
        back_populates="owner",
        cascade="all, delete-orphan",
    )