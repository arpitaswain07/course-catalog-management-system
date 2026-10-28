from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:03012011sai%23@localhost/coursecatalogdb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()

print("Database connected successfully!")

try:
    with engine.connect() as connection:
        print("Database connected successfully!")
except Exception as e:
    print("Connection failed!")
    print(e)
