from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker,declarative_base

# DATABASE_URL="postgresql://postgres:Sanket123@localhost:5432/hms"
DATABASE_URL="postgresql://hms_ihbr_user:OftZ6bH3SVKnGNNOdC1pG7y4PvVz1kji@dpg-d8fs8in40ujc73bd6a80-a.oregon-postgres.render.com/hms_ihbr"

engine = create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()
