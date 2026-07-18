from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped,mapped_column, relationship

from app.db.database import Base


class Task(Base):
    __tablename__="tasks"

    id:Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner = relationship("User",back_populates="tasks")