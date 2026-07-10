from sqlalchemy import create_engine
from app.core.config import settings
from sqlalchemy.orm import DeclarativeBase, sessionmaker


engine = create_engine(
    settings.database_url,
    echo=True,
)


sessionLocal =  sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)



class Base(DeclarativeBase):
    pass