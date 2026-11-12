from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Set DATABASE_URL in .env to use PostgreSQL.
DATABASE_URL = "postgresql+psycopg://admin:supersecret@localhost:5432/print_analytics"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

def get_session():
    return SessionLocal()

# def init_db():
#     # Import models before create_all so SQLAlchemy knows all tables.
#     import models  # noqa: F401
#     # Base.metadata.create_all(bind=engine)
